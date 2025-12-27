# 🛡️ Network Intrusion Detection System (NIDS)

## 📌 Overview
A **Machine Learning–based Network Intrusion Detection System (NIDS)** that classifies network traffic as **normal or malicious**.  
The system uses **classical machine learning and deep learning models** trained on the **NSL-KDD benchmark dataset** to detect network attacks.

Designed with a **modular pipeline** focusing on preprocessing, model training, evaluation, and comparison.

---

## 🚀 Features
- Binary classification: **Normal vs Attack**
- Classical and deep learning models
- Trained on **NSL-KDD dataset**
- Model comparison and analysis
- Modular and extensible ML pipeline

---

## 🧠 Models Used
- **LSTM (Long Short-Term Memory)**
- **RNN (Recurrent Neural Network)**
- **KNN (K-Nearest Neighbors)** — baseline model

Deep learning models capture **sequential patterns** in network traffic, improving detection over traditional ML approaches.

---

## 📊 Dataset
- **Name:** NSL-KDD
- **Type:** Intrusion detection benchmark dataset
- **Features:** 41 network traffic attributes
- **Classes:** Normal traffic and multiple attack categories

---

## 🛠️ Tech Stack
- **Language:** Python
- **Libraries:** NumPy, Pandas, Scikit-learn
- **Deep Learning:** TensorFlow / Keras
- **Tools:** Jupyter Notebook, Google Colab

---

## ⚙️ Pipeline
1. Data preprocessing and feature encoding
2. Train-test split
3. Model training (KNN, RNN, LSTM)
4. Evaluation and comparison

---

## 📈 Results
| Model | Accuracy |
|------|----------|
| KNN  | XX% |
| RNN  | XX% |
| LSTM | XX% |

> Exact evaluation metrics can be updated after final experimentation.

---

## 📂 Project Structure
NIDS/
├── data/
├── preprocessing/
├── models/
├── evaluation/
├── notebooks/
└── README.md

---

## 🔮 Future Work
- Real-time packet capture and classification
- Live network traffic integration
- Low-latency model optimization
- API-based deployment

---

## 🎯 Use Cases
- Enterprise network security
- Intrusion detection research
- Foundation for real-time IDS deployment

---

## 👤 Author
**Het Bhutak**  
AI/ML Engineer  

- GitHub: https://github.com/Hettbhutak  
- LinkedIn: https://linkedin.com/in/het-bhutak-3101601ba
