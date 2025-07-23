# 📊 Sales Prediction Using Machine Learning

✅ **3 out of 3 projects successfully completed under the Oasis Infobyte Data Science Internship.**

This project predicts product sales based on advertising spend across **TV**, **Radio**, and **Newspaper** using a **Linear Regression model**. It includes a **Streamlit web app** for real-time, interactive predictions. The model is trained using the popular ISLR Advertising dataset.

---

## 📁 Folder Structure

```
sales_prediction/
├── dataset.csv           # Advertising dataset
├── model_training.py     # Python script to train and save the ML model
├── sales_model.pkl       # Trained and saved model (generated after training)
├── app.py                # Streamlit app for live sales prediction
└── requirements.txt      # Project dependencies
```

---

## 🚀 Features

- ✅ Trains a regression model using real-world advertising data
- 📊 Visualizes feature relationships and model performance
- 🤖 Predicts product sales using Linear Regression
- 🌐 Streamlit-based interactive prediction interface
- 💾 Model saved and reused with `pickle`

---

## 🛠️ Technologies Used

- **Python 3**
- **Pandas**, **NumPy** – Data manipulation
- **Matplotlib**, **Seaborn** – Data visualization
- **Scikit-learn** – Machine learning
- **Streamlit** – Web interface

---

## ⚙️ How to Run the Project

### 1. Clone the Repository

```bash
git clone https://github.com/Anushka-751/sales-prediction.git
cd sales-prediction
```

### 2. Install Required Packages

```bash
pip install -r requirements.txt
```

### 3. Train the Machine Learning Model

```bash
python model_training.py
```

This command trains the Linear Regression model and saves it as `sales_model.pkl`.

### 4. Run the Streamlit App

```bash
streamlit run app.py
```

---

## 📂 Dataset Description

| Feature     | Description                               |
|-------------|-------------------------------------------|
| TV          | Advertising budget for TV (in thousands)  |
| Radio       | Advertising budget for Radio (in thousands) |
| Newspaper   | Advertising budget for Newspaper (in thousands) |
| Sales       | Actual product sales (target variable)    |

