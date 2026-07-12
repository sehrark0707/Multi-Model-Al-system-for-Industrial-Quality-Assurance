import streamlit as st
from ultralytics import YOLO
from PIL import Image
import ollama
from datetime import date
import cv2
import numpy as np

# Set up the web page
st.set_page_config(page_title="QA System", layout="wide")
st.title("AI-Powered Industrial Quality Assurance")

# Load your trained YOLO model
@st.cache_resource
def load_model():
    return YOLO('best.pt')

model = load_model()

# Create a file uploader
uploaded_file = st.file_uploader("Upload a steel surface image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Uploaded Image")
        st.image(image, use_container_width=True)
        
    # 1. Run YOLOv8 detection
    results = model(image)
    
    # 2. Draw boxes on the image
    res_image = results[0].plot()
    res_image = cv2.cvtColor(res_image, cv2.COLOR_BGR2RGB) # Fix colors for Streamlit
    
    with col2:
        st.subheader("Detected Defects")
        st.image(res_image, use_container_width=True)
        
    # 3. Extract the names and confidences of what YOLO found
    defects = []
    for box in results[0].boxes:
        class_id = int(box.cls[0])
        conf = float(box.conf[0])
        class_name = model.names[class_id]
        defects.append(f"{class_name} ({conf*100:.0f}%)")
        
    # 4. Generate the Report using Llama 3.2
    st.divider()
    st.subheader("Inspection Report")
    
    if defects:
        with st.spinner("AI is generating the maintenance report..."):
            today = date.today().strftime("%d %B %Y")
            
            # The prompt telling Llama exactly how to format the output
            prompt = f"""
            You are an Industrial Quality Assurance AI. Generate a professional inspection report based on the following detected defects on a steel sheet: {', '.join(defects)}. 
            
            Format the output EXACTLY like this:
            
            **Inspection Date:** {today}
            
            **Detected Defects:**
            [List the defects as bullet points with their percentages]
            
            **Summary:**
            [Provide a 2-sentence summary of the surface quality]
            
            **Severity:**
            [Low, Medium, or High]
            
            **Recommended Action:**
            [Provide 3-4 bullet points for recommended actions]
            """
            
            # Send the prompt to your local Ollama instance
            response = ollama.chat(model='llama3.2', messages=[
                {'role': 'user', 'content': prompt}
            ])
            
            # Display the text Llama generates
            st.markdown(response['message']['content'])
    else:
        st.success("No defects detected. The steel surface is clean.")