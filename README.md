:

📊 Sales Prediction Using Machine Learning
This project predicts sales based on advertising spend across TV, Radio, and Newspaper using a linear regression model. A user-friendly Streamlit interface is also included for real-time predictions.

📁 Folder Structure
bash
Copy code
sales_prediction/
├── dataset.csv
├── model_training.py     # Trains and saves model as sales_model.pkl
├── sales_model.pkl       # Trained ML model (auto-generated)
├── app.py                # Streamlit UI to predict sales
└── requirements.txt      # Dependencies
🚀 Features
📉 Trains a regression model using real-world advertising data

📊 Visualizes data and model performance

✅ Predicts sales from advertising inputs via a Streamlit web app

💾 Saves the model as a .pkl file for future use

📦 Requirements
Install all dependencies using:

bash
Copy code
pip install -r requirements.txt
🛠 Technologies Used
Python

Pandas, NumPy

Matplotlib, Seaborn

Scikit-learn

Streamlit

⚙️ How to Run
1. Train the Model
bash
Copy code
python model_training.py
This generates sales_model.pkl.

2. Launch the Streamlit App
bash
Copy code
streamlit run app.py
📸 UI Demo
Add a screenshot of your Streamlit app here once ready.

📚 Dataset
The dataset used contains advertising spend and corresponding sales values across various channels:

TV

Radio

Newspaper

Sales (target)

Dataset source: Advertising Data from ISLR

✅ Outcomes
Achieved high R² score using Linear Regression

Successfully deployed a no-code web app for dynamic sales prediction

🙋‍♀️ Developed By
Anushka A Poojary
🎓 B.E. Computer Science | Full Stack + ML Enthusiast
🔗 LinkedIn
💻 GitHub

