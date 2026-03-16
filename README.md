# Insulator Detection System Based on YOLOv8

## Introduction

This project implements a basic computer vision system for detecting power transmission line insulators using deep learning. The system is built based on the YOLOv8 object detection model and the PyTorch deep learning framework.

The purpose of this project is to explore and implement the complete workflow of an object detection task, including dataset collection, image annotation, dataset format conversion, model training, and object detection.

The trained model can detect insulators in images, videos, and real-time camera streams. This project serves as a practical example of applying computer vision techniques to power equipment inspection.

---

## Features

- Dataset collection and preprocessing
- Manual data annotation using Labelme
- Dataset format conversion for YOLO training
- YOLOv8 model training
- Image detection
- Video detection
- Real-time camera detection
- Visualization of detection results

---

## Project Workflow

The project follows a standard computer vision development pipeline:

1. Dataset collection
2. Data annotation using Labelme
3. Dataset format conversion
4. Model training with YOLOv8
5. Model inference and object detection
6. Real-time camera detection

---

## Technologies Used

- Python
- YOLOv8
- PyTorch
- OpenCV
- Labelme

---

## Project Structure

insulator-detection

dataset/               # image dataset and labels  
models/                # trained model files  

train.py               # model training script  
detect.py              # image or video detection  
camera_detect.py       # real-time camera detection  

requirements.txt       # project dependencies  
README.md              # project documentation  

---

## Installation

Clone the repository:

git clone https://github.com/chengcheng-2006/insulator-detection.git

Install required dependencies:

pip install -r requirements.txt

---

## Usage

Train the model:

python train.py

Run image detection:

python detect.py

Run real-time camera detection:

python camera_detect.py

---

## Future Improvements

Possible future improvements include:

- Expanding the dataset with more training images
- Improving detection accuracy through parameter tuning
- Adding defect detection for damaged insulators
- Developing a simple web-based interface for visualization

---

## Notes

This project is mainly developed for learning and practice in computer vision and deep learning.
