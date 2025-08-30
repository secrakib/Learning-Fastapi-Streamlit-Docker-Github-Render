import streamlit as st
import requests
import os

# Get backend URL from environment variable (default to localhost)
BACKEND_URL = os.getenv("BACKEND_URL", "http://localhost:8000")
print("Backend url ==" + BACKEND_URL)

st.title("🏦 Banknote Authentication")

st.write("Enter the features to check if a banknote is **Fake** or **Okay**.")

# Input fields
variance = float(st.text_input("Variance", "0"))
skewness = float(st.text_input("Skewness", "0"))
curtosis = float(st.text_input("Curtosis", "0"))
entropy = float(st.text_input("Entropy", "0"))


if st.button("Predict"):
    # Prepare JSON payload
    data = {
        "variance": variance,
        "skewness": skewness,
        "curtosis": curtosis,
        "entropy": entropy
    }

    try:
        response = requests.post(f"{BACKEND_URL}/predict", json=data)
        if response.status_code == 200:
            st.success(f"Prediction: {response.json()}")
        else:
            st.error(f"Error from backend: {response.text}")
    except requests.exceptions.RequestException as e:
        st.error(f"Could not connect to backend: {e}")
