# 📊 Sales Prediction Using Machine Learning

This project predicts product sales based on advertising spend across **TV**, **Radio**, and **Newspaper** channels using a **Linear Regression model**. It includes a **Streamlit web app** for user-friendly real-time predictions.

---

## 📁 Folder Structure

sales_prediction/
├── dataset.csv # Advertising dataset
├── model_training.py # Trains and saves the ML model
├── sales_model.pkl # Saved trained model (generated after training)
├── app.py # Streamlit UI for prediction
└── requirements.txt # Python dependencies

yaml
Copy code

---

## 🚀 Features

- 📈 Trains a regression model on historical advertising data
- 🧠 Uses Linear Regression to model the relationship between ad spend and sales
- 📊 Displays performance metrics (R² score, MSE) and visualizations
- 🌐 Streamlit app for real-time prediction with user inputs
- 💾 Model persistence using `pickle`

---

## 🛠️ Technologies Used

- **Python 3**
- **Pandas, NumPy** – Data handling
- **Matplotlib, Seaborn** – Data visualization
- **Scikit-learn** – Machine learning
- **Streamlit** – Web app interface

---

## ⚙️ How to Run the Project

### 1. Clone the Repository

```bash
git clone https://github.com/Anushka-751/sales-prediction.git
cd sales-prediction
2. Install Dependencies
bash
Copy code
pip install -r requirements.txt
3. Train the Model
bash
Copy code
python model_training.py
This will train the Linear Regression model and save it as sales_model.pkl.

4. Launch the Streamlit App
bash
Copy code
streamlit run app.py
📷 Demo Screenshot
(Insert a screenshot of your Streamlit app here)

📂 Dataset Info
Feature	Description
TV	Advertising spend on TV (in $)
Radio	Advertising spend on Radio (in $)
Newspaper	Advertising spend on Newspaper (in $)
Sales	Sales figures (target variable)

📌 Source: ISLR Advertising Dataset

✍️ Author
Anushka A Poojary
🎓 B.E. Computer Science Engineering
🌐 LinkedIn
💻 GitHub

📌 License
This project is licensed under the MIT License.

