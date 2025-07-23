# 📊 Sales Prediction Using Machine Learning

✅ **3 out of 3 projects successfully completed under the Oasis Infobyte Data Science Internship**.

This project predicts product sales based on advertising spend across **TV**, **Radio**, and **Newspaper** using a **Linear Regression model**. It includes a **Streamlit web app** for real-time, interactive predictions. The goal is to understand how different advertising budgets affect sales and to build a model that can forecast sales accurately.

---

## 📁 Folder Structure

sales_prediction/
├── dataset.csv # Advertising dataset
├── model_training.py # Python script to train and save the ML model
├── sales_model.pkl # Trained and saved model (generated after training)
├── app.py # Streamlit app for live sales prediction
└── requirements.txt # Project dependencies

yaml
Copy code

---

## 🚀 Features

- ✅ Trains a regression model using real-world advertising data
- 📊 Visualizes data relationships and model performance
- 🤖 Uses Linear Regression to forecast sales
- 🌐 Deploys a Streamlit app for user-friendly prediction
- 💾 Saves the trained model using `pickle` for reuse

---

## 🛠️ Technologies Used

- **Python 3**
- **Pandas**, **NumPy** – Data handling
- **Matplotlib**, **Seaborn** – Data visualization
- **Scikit-learn** – Machine Learning (Linear Regression)
- **Streamlit** – Web-based UI for predictions

---

## ⚙️ How to Run the Project

### 1. Clone the Repository
```bash
git clone https://github.com/Anushka-751/sales-prediction.git
cd sales-prediction
```
2. Install Dependencies
```bash
pip install -r requirements.txt
```
4. Train the Model
```bash

python model_training.py
This command trains the Linear Regression model and saves it as sales_model.pkl.
```
5. Launch the Streamlit Web App
```bash
streamlit run app.py
```
📂 Dataset Information
Feature	Description
TV	Advertising spend on TV (in $)
Radio	Advertising spend on Radio (in $)
Newspaper	Advertising spend on Newspaper (in $)
Sales	Product sales (target variable)
