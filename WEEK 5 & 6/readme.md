Week 5 and 6 Exploratory Data Analysis and Computer Vision

Over these two weeks the primary objective was transitioning from analyzing raw data to training a custom object detection model.

Prior to working with AI models I focused on Exploratory Data Analysis and data cleaning. For this type of image dataset EDA goes beyond basic spreadsheets. It requires analyzing image distribution and checking for class imbalances to ensure equal representation of all defect categories like scratches and crazing. It also involves verifying that bounding box labels align accurately with the physical defects on the steel surfaces.

After preparing the data I advanced to the computer vision stage. I selected the YOLOv8 architecture due to its exceptional speed and high accuracy for real-time object detection. I utilized Google Colab to train the model on the NEU Surface Defect Database from Kaggle because local machine training is too time-consuming.

I tested various model sizes including YOLOv8-nano and YOLOv8-medium. This testing phase helped me find the optimal balance between inference speed and detection accuracy.

The final model achieved the following performance metrics

Precision [0.666]

Recall [0.783]

mAP@50 [0.799]

mAP@50-95 [0.506]

This folder contains a metrics_screenshots directory displaying training curves confusion matrices and sample predictions to illustrate the learning progress over time. The final trained model weights are stored here as best.pt.
