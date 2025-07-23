# app.py

import streamlit as st
import pickle
import numpy as np

# Load the model
with open("sales_model.pkl", "rb") as file:
    model = pickle.load(file)

# App title
st.title(" Sales Prediction App")
st.write("Enter the advertising spend for each channel to predict sales.")

# Input fields
tv = st.number_input("TV Advertising Spend (in $)", min_value=0.0, format="%.2f")
radio = st.number_input("Radio Advertising Spend (in $)", min_value=0.0, format="%.2f")
newspaper = st.number_input("Newspaper Advertising Spend (in $)", min_value=0.0, format="%.2f")

# Predict button
if st.button("Predict Sales"):
    input_data = np.array([[tv, radio, newspaper]])
    prediction = model.predict(input_data)
    st.success(f" Predicted Sales: {prediction[0]:.2f} units")
