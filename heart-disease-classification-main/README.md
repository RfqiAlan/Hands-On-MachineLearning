# heart-disease-classification
Heart Disease Prediction using Machine Learning (Classification)

📌Project Overview

Heart disease is one of the leading causes of death worldwide. Early detection can help in timely medical intervention.
This project focuses on building a machine learning classification model to predict the presence of heart disease using patient health data.
The project compares multiple classification algorithms and selects the best-performing model based on appropriate evaluation metrics for healthcare data.

🎯 Objective

Predict whether a patient has heart disease (0 = No, 1 = Yes)

Compare different classification models

Select the most suitable model using ROC-AUC and accuracy

📊 Dataset

Source: Healthcare heart disease dataset from Kaggle

Records contain demographic and clinical attributes such as:

Age

Sex

Chest pain type

Blood pressure

Cholesterol

Heart rate

ECG results

Target variable: heart_disease (binary)
The dataset shows moderate class imbalance, which is common in real-world medical data.

🛠️ Technologies Used

Python

NumPy

Pandas

Scikit-learn

Matplotlib

Seaborn

🔍 Project Workflow

Data loading and inspection

Data cleaning (handling missing values and duplicates)

Feature scaling using StandardScaler

Train–test split

Model training and evaluation

Model comparison and selection

Final visualization using ROC curve

🤖 Models Implemented

Logistic Regression (baseline model)

Random Forest Classifier

Gradient Boosting Classifier (final model)

📈 Model Evaluation

The models were evaluated using:

Accuracy

ROC-AUC score

Precision, Recall, and F1-score

Confusion Matrix

🔹 Final Results

Model	Accuracy	ROC-AUC

Logistic Regression	~0.64	~0.67

Random Forest	~0.62	~0.65

Gradient Boosting	~0.66	~0.68

Gradient Boosting Classifier was selected as the final model due to the best ROC-AUC performance.

🧠 Key Learnings

Classification is more appropriate than regression for heart disease prediction

ROC-AUC is a better metric than accuracy for imbalanced medical datasets

Simpler models like Logistic Regression can perform competitively

Ensemble models improve stability and generalization

📌 Conclusion

This project demonstrates a complete end-to-end machine learning classification pipeline for a real-world healthcare problem.

The results are realistic and highlight the challenges involved in medical prediction tasks.

🚀 Future Improvements

Hyperparameter tuning

Threshold optimization to improve recall

Cross-validation for more robust evaluation

Model explainability using SHAP

📂 How to Run

Clone the repository

Install required libraries

Run the notebook or Python script step by step

👩‍💻 Author

Jibi Mol K A
Aspiring Data Scientist 
