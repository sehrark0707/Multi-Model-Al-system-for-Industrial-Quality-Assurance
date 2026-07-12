### Multi-Model AI System

This project is an AI-powered quality checker for factory assembly lines. Instead of relying solely on people to manually inspect products, the system uses a camera to spot defects automatically. Afterward, it uses a smart text AI to write up a professional maintenance report.

**Week 1: Getting Started with Code and AI Concepts**
I kicked things off by setting up my coding workspace on Google Colab and Kaggle. I brushed up on my Python skills, writing simple scripts to get back into the groove. I also spent some time reading about how machine learning actually works behind the scenes—basically, how computers learn from data instead of just following strict rules.

**Week 2: Hands-On Machine Learning**
This week was all about getting my hands dirty with data. I learned how to organize and sort through large datasets using a tool called Pandas. I also played around with different types of AI models to see how they behave. A big part of this week was learning how to properly test a model so it actually learns the patterns instead of just memorizing the answer key.

**Week 3: Deep Learning and Image Processing**
I dove straight into deep learning, specifically focusing on how AI looks at pictures (called Convolutional Neural Networks). Since my project needs to visually inspect factory items, I had to understand how the AI breaks down an image pixel by pixel to recognize shapes, edges, and patterns. This was a massive step for building the "eyes" of the system.

**Week 4: Enter the Text AI (LLMs)**
This week, I shifted my focus to Large Language Models (like ChatGPT) to see how they work in the real world. My main goal was figuring out how to connect a text AI with the vision AI I learned about last week. The game plan was simple: the vision model spots the physical flaw, and the text model writes a clear explanation of it.

**Week 5 and 6: Prepping Data and Training the Vision Model**
For these two weeks, I got down to business. I started by cleaning up my dataset (pictures of steel surfaces) and making sure all the defects were labeled correctly. Once the data was ready, I trained a popular object detection model called YOLOv8 to recognize specific manufacturing flaws like scratches and pitted surfaces. I tested a few different versions of the model to find the sweet spot between being fast and being accurate, and saved the best one for my final app.

**Week 7 and 8: Bringing It All Together in a Web App**
This was the final stretch where everything clicked into place. I built a simple web application using a tool called Streamlit, giving factory inspectors an easy way to upload a photo of a steel sheet.

Here is how it works: when an image is uploaded, the vision model scans it and highlights any defects. It then hands that information over to a text AI (Llama 3.2) running locally on the computer. This AI acts like a virtual quality assurance expert, automatically writing up a professional inspection report that explains how bad the damage is and what maintenance steps should be taken next.
