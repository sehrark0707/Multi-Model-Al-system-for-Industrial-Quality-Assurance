Week 7 and 8 LLM Integration and Web Deployment

This final project phase transforms the standalone AI model into a fully functional web application. I built a user interface with Streamlit rather than relying on Jupyter notebooks allowing an inspector to use this tool directly on the factory floor.

The application integrates two distinct types of AI

Computer Vision When a user uploads a steel sheet image the custom YOLOv8 model developed in week 6 scans it to draw bounding boxes around any surface defects.

Large Language Model (LLM) The application extracts the names and confidence scores of the detected defects and inputs them into a local Llama 3.2 model. The LLM functions as a quality assurance expert by generating a formatted inspection report containing a summary severity level and recommended maintenance actions.

I selected Ollama to execute the Llama model locally. This approach offers a significant advantage for industrial environments because the data remains securely on the computer. It eliminates the need for an internet connection or paid cloud APIs to generate reports.

Follow these steps to run this project on your local machine

Download and run the local LLM
Install Ollama from their official website. Next open your terminal and execute the following command

ollama run llama3.2

This prompts Ollama to download the Llama 3.2 model to your system. The file size is several gigabytes so allow it time to complete. Once finished it will open a chat prompt where you can simply type /bye to exit. The model will then remain ready in the background.

Install the required Python packages
Ensure your terminal is navigated to this project folder and run

pip install -r requirements.txt

This command reads the text file to install all necessary libraries including Streamlit for the web application Ultralytics for YOLO and OpenCV for image processing.

Start the application
Once all installations are complete start the local server with

python -m streamlit run app.py

Using the python -m prefix is highly recommended as it helps avoid common Windows PATH errors.

After the server starts a new browser tab will open where you can upload steel images and test the entire pipeline.

Since the best.pt file is too large to upload to github, I've added it to a drive link and it is to be with the app.py file in order to streamlit to run localhost
https://drive.google.com/file/d/11jo4cCmre9wV-Sz0zTYKrhVOWBTODwrP/view?usp=sharing
