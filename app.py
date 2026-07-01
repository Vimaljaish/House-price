import streamlit as st
import pickle
import numpy as np

# Load the trained model
with open("model_pk1", "rb") as file:
    model = pickle.load(file)

# Page configuration
st.set_page_config(
    page_title="House Price Prediction",
    page_icon="🏠",
    layout="centered"
)

st.title("🏠 House Price Prediction")
st.write("Enter the house details below to predict the price.")

# User Inputs
area = st.number_input("Area (sq ft)", min_value=100, value=1000)
bedrooms = st.number_input("Number of Bedrooms", min_value=1, max_value=10, value=2)
bathrooms = st.number_input("Number of Bathrooms", min_value=1, max_value=10, value=1)

# Prediction Button
if st.button("Predict Price"):
    input_data = np.array([[area, bedrooms, bathrooms]])
    prediction = model.predict(input_data)

    st.success(f"Predicted House Price: ₹ {prediction[0]:,.2f}")

st.markdown("---")
st.caption("Developed using Streamlit and Scikit-learn")
