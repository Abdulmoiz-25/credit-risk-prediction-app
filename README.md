# 📘 DeveloperHub Task 2 – Credit Risk Prediction using ML  

## 📌 Task Objective  
This task focuses on building a credit scoring model to predict whether a loan applicant is likely to default or not based on financial and demographic history using supervised machine learning.

---

## 📁 Dataset  
**Name**: Credit Risk Dataset  
**Source**: Kaggle  

### 📊 Features:
- `Gender`  
- `Married`  
- `Education`  
- `Self_Employed`  
- `ApplicantIncome`  
- `CoapplicantIncome`  
- `LoanAmount`  
- `Loan_Amount_Term`  
- `Credit_History`  
- `Property_Area`  

### 🎯 Target:
- `Loan_Status` (Y/N – indicating default risk)

---

## 🛠️ Tools & Libraries Used  
- **Pandas** – Data loading & cleaning  
- **Matplotlib & Seaborn** – Visualizations  
- **Scikit-learn** – Model training and evaluation  
- **Streamlit** – Web-based app for deployment  
- **Pickle** – Saving trained model for inference  

---

## 🚀 Approach  

### 1. Dataset Loading & Understanding  
- Loaded the dataset using `pandas.read_csv()`  
- Inspected with `.head()`, `.info()`, `.describe()`, `.shape()`  

### 2. Data Cleaning & Preparation  
- Handled missing values (mean/mode imputation)  
- Encoded categorical variables using Label Encoding  
- Feature scaling applied if needed  

### 3. Exploratory Data Analysis (EDA)  
- Bar plots for categorical distribution  
- Histograms and box plots for numerical features  
- Correlation heatmaps  
- Distribution of target class  

### 4. Model Training & Testing  
- Split data into 80% training and 20% testing  
- Trained with:
  - Logistic Regression  
  - Decision Tree Classifier  
  - Random Forest Classifier  
- Saved the best-performing model using `pickle`  

### 5. Evaluation Metrics  
- Accuracy Score  
- Confusion Matrix  
- Classification Report  
- ROC Curve  

---

## 📊 Results & Insights  
- **Random Forest** outperformed other models in accuracy.  
- **Key predictors**: `Credit_History`, `ApplicantIncome`, and `LoanAmount`  
- **Balanced preprocessing** played a critical role in improving model performance  

---

## ✅ Conclusion  
This task demonstrated the full ML workflow:  
- Data preprocessing  
- EDA  
- Model training  
- Evaluation  
- Deployment

The final model helps automate initial screening for loan applications by predicting potential defaults.

---

## 🖥️ Streamlit Web App  
Try the deployed model here:  
🔗 [Streamlit App](https://credit-risk-prediction-app-lbnmqjjdhm4nnf6sefg8w8.streamlit.app/)

---

## 🔗 Useful Links  
- [Scikit-learn Documentation](https://scikit-learn.org/)  
- [Streamlit Docs](https://docs.streamlit.io/)  
- [Matplotlib Docs](https://matplotlib.org/)  
- [Seaborn Docs](https://seaborn.pydata.org/)  

---

> 🔖 Submitted as part of the **Developer Hub Internship Program**


