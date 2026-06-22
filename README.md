# 🩺 Diabetes Prediction using Machine Learning & Fuzzy Logic

A machine learning project that predicts the likelihood of diabetes in patients using clinical data. Built with Logistic Regression for binary classification and enhanced with a Fuzzy Logic system for interpretable risk scoring — going beyond a standard prediction model to provide explainable AI outputs.

> **Achieved 78.1% accuracy** on the PIMA Indians Diabetes Dataset using Logistic Regression with proper preprocessing and outlier removal.

---

## 📌 Project Overview

Diabetes affects over 537 million people worldwide and is a leading cause of blindness, kidney failure, and heart disease. Early prediction using patient data can significantly improve outcomes — especially in regions like Pakistan where access to specialist diagnosis is limited.

This project builds a complete ML pipeline that:
- Cleans and preprocesses clinical data
- Trains a Logistic Regression classifier
- Evaluates model performance with multiple metrics
- Adds a **Fuzzy Logic layer** that converts raw glucose readings into interpretable risk scores — making predictions understandable to non-technical users like doctors or patients

---

## ✨ Key Features

| Feature | Description |
|---|---|
| Data Preprocessing | Replaces invalid zero values with column medians, removes outliers using IQR |
| ML Model | Logistic Regression with StandardScaler normalization |
| Model Accuracy | 78.1% on test set |
| Fuzzy Logic System | Converts glucose levels into risk scores using membership functions |
| Modular Code | Clean separation into `data_processing.py`, `model_training.py`, `fuzzy_logic.py`, `main.py` |

---

## 🗂️ Project Structure

```
Diabetes-Prediction/
│
├── data_processing.py     # Data loading, cleaning, outlier removal
├── model_training.py      # Model training, scaling, evaluation
├── fuzzy_logic.py         # Fuzzy Logic risk scoring system
├── main.py                # Main runner — full pipeline output
├── diabetes.csv           # PIMA Indians Diabetes Dataset
└── README.md
```

---

## 📊 Dataset

**PIMA Indians Diabetes Dataset** — originally from the National Institute of Diabetes and Digestive and Kidney Diseases (USA).

- 768 patient records
- 8 input features: Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age
- 1 output: Outcome (1 = Diabetic, 0 = Non-diabetic)

> Source: [Kaggle — PIMA Indians Diabetes Database](https://www.kaggle.com/datasets/uciml/pima-indians-diabetes-database)

**Important preprocessing note:** Several features (Glucose, BloodPressure, BMI, Insulin, SkinThickness) contain 0 values that are biologically impossible — these represent missing data. This project replaces those zeros with column medians before training, which meaningfully improves model accuracy compared to leaving them in.

---

## ⚙️ How It Works

### Step 1 — Data Processing (`data_processing.py`)
- Loads the CSV dataset
- Replaces impossible zero values with column medians
- Removes statistical outliers using the IQR (Interquartile Range) method
- Splits data into features (X) and labels (y)

### Step 2 — Model Training (`model_training.py`)
- Splits data: 80% training / 20% testing
- Applies `StandardScaler` to normalize all features
- Trains a `LogisticRegression` model (`max_iter=1000`)
- Evaluates with accuracy score, precision, recall, and F1-score

### Step 3 — Fuzzy Logic Risk Scoring (`fuzzy_logic.py`)
- Defines glucose membership functions: **Low** (0–100), **Normal** (80–140), **High** (120–200)
- Calculates how much a patient's glucose value belongs to each category
- Outputs a continuous risk score and a human-readable risk label
- Example: Glucose = 150 → Risk Score: 27.5

---

## 🚀 Getting Started

### Prerequisites
```bash
pip install -r requirements.txt
```

### Requirements (`requirements.txt`)
```
pandas
numpy
scikit-learn
scikit-fuzzy
```

### Run the full pipeline
```bash
python main.py
```

---

## 📈 Actual Results

```
Model Accuracy: 0.78125

Classification Report:
              precision    recall  f1-score   support

           0       0.79      0.92      0.85        85
           1       0.76      0.51      0.61        43

    accuracy                           0.78       128
   macro avg       0.77      0.71      0.73       128
weighted avg       0.78      0.78      0.77       128

Fuzzy Diabetes Risk for glucose=150: 27.5
```

### Results Summary

| Metric | Class 0 (No Diabetes) | Class 1 (Diabetic) |
|---|---|---|
| Precision | 0.79 | 0.76 |
| Recall | 0.92 | 0.51 |
| F1 Score | 0.85 | 0.61 |
| **Overall Accuracy** | **78.1%** | |

**Key observation:** The model performs stronger on identifying non-diabetic patients (recall 0.92) than diabetic ones (recall 0.51). This class imbalance is a known challenge with the PIMA dataset — future work could address this using SMOTE oversampling or ensemble methods like Random Forest or XGBoost to improve diabetic recall.

---

## 🔬 Why Fuzzy Logic?

Standard ML models output a binary answer: diabetic or not. This works statistically but gives no nuance — a patient with glucose of 126 and a patient with glucose of 198 both get classified as "Diabetic" with no indication that their risk levels are very different.

Fuzzy Logic addresses this by treating categories as overlapping gradients rather than hard boundaries. A glucose reading of 126 might be 60% "Normal" and 40% "High" — and the system outputs a proportional risk score that reflects this uncertainty. This makes the system more useful in clinical settings where doctors need degree of risk, not just yes/no.

This combination of ML + Fuzzy Logic is a step toward **Explainable AI (XAI)** — an active area of research in healthcare AI.

---

## 🛠️ Tech Stack

![Python](https://img.shields.io/badge/Python-3.14-blue)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-ML-orange)
![scikit-fuzzy](https://img.shields.io/badge/scikit--fuzzy-FuzzyLogic-green)
![Pandas](https://img.shields.io/badge/Pandas-DataProcessing-lightblue)
![NumPy](https://img.shields.io/badge/NumPy-Numeric-yellow)
![VSCode](https://img.shields.io/badge/VSCode-Editor-blue)

---

## 🌍 Real-World Relevance

Pakistan has one of the highest diabetes prevalence rates in the world — approximately 30% of adults aged 25–70 are affected (IDF Diabetes Atlas 2021). Affordable, accessible early-warning tools built on clinical data could assist primary healthcare workers in screening patients before specialist referral. This project is a small step toward that goal.

---

## 🔮 Future Improvements

- Try Random Forest and XGBoost to improve recall for diabetic class (currently 0.51)
- Apply SMOTE to handle class imbalance in the dataset
- Build a web app using Streamlit so users can enter values and get predictions
- Extend Fuzzy Logic to use multiple features (not just glucose) for a more complete risk score

---

## 👤 Author

**Abdul Manan**
BS Computer Science — Final Year Student
Passionate about AI/ML applications in healthcare and low-resource settings.

📧 Connect on [GitHub](https://github.com/manan8t8)

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

## 🙏 Acknowledgements

- PIMA Indians Diabetes Dataset — National Institute of Diabetes and Digestive and Kidney Diseases
- Scikit-learn documentation
- scikit-fuzzy library contributors
