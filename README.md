🛡️ Network Intrusion Detection System (NIDS)
📌 Overview

This project implements a Machine Learning–based Network Intrusion Detection System (NIDS) to classify network traffic as normal or malicious.
The system is designed to enhance cybersecurity by detecting attacks using supervised learning models trained on a benchmark dataset.

The project focuses on feature-driven attack detection, model comparison, and practical applicability in real-world network environments.

🚀 Features

Classifies network traffic into normal vs attack

Uses deep learning and classical ML models

Trained and evaluated on the NSL-KDD dataset

Comparative analysis of multiple algorithms

Modular pipeline for data preprocessing, training, and evaluation

🧠 Models Implemented

K-Nearest Neighbors (KNN) – baseline model

Recurrent Neural Network (RNN)

Long Short-Term Memory (LSTM)

Deep learning models are used to capture temporal patterns in network traffic data.

📊 Dataset

Dataset: NSL-KDD

Description: Improved version of the KDD’99 dataset, widely used for intrusion detection research

Features: 41 network traffic attributes

Classes: Normal traffic and multiple attack types

🛠️ Tech Stack

Programming Language: Python

Libraries & Frameworks:

NumPy, Pandas

Scikit-learn

TensorFlow / Keras

Environment: Jupyter Notebook / Google Colab

⚙️ Workflow

Data preprocessing and feature encoding

Train-test split

Model training (KNN, RNN, LSTM)

Performance evaluation

Result comparison

📈 Results
Model	Purpose
KNN	Baseline performance comparison
RNN	Sequential pattern learning
LSTM	Improved long-term dependency learning

LSTM and RNN models demonstrated better performance compared to traditional ML approaches due to their ability to model sequential network behavior.

(You can later add exact accuracy values when finalized)

📂 Project Structure
NIDS/
│── data/
│── preprocessing/
│── models/
│── evaluation/
│── notebooks/
│── README.md

🔮 Future Improvements

Real-time packet capture and classification

Integration with live network traffic

Model optimization for low-latency detection

Deployment as an API-based security service

🎯 Use Case

Enterprise network security

Research and academic experimentation

Foundations for real-time IDS deployment

🧑‍💻 Author

Het Bhutak
AI/ML Engineer
🔗 GitHub: https://github.com/Hettbhutak

🔗 LinkedIn: https://linkedin.com/in/het-bhutak-3101601ba
