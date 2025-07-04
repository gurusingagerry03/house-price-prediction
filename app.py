import streamlit as st
import requests

API_URL = "https://web-production-f037.up.railway.app/predict"

st.title("🏠 House Price Prediction")

# User Inputs
area = st.number_input("Living Area (GrLivArea)", min_value=300, max_value=5000, value=1000)
bedrooms = st.selectbox("Number of Bedrooms", [1, 2, 3, 4, 5])
bathrooms = st.selectbox("Number of Full Bathrooms", [1, 2, 3])
garage = st.selectbox("Garage Capacity (Cars)", [0, 1, 2, 3])
year = st.slider("Year Built", 1870, 2023, 2000)

if st.button("Predict Price"):
    payload = {
        "GrLivArea": area,
        "BedroomAbvGr": bedrooms,
        "FullBath": bathrooms,
        "GarageCars": garage,
        "YearBuilt": year
    }
    try:
        res = requests.post(API_URL, json=payload)
        if res.status_code == 200:
            result = res.json()
            st.success(f"💰 Predicted Price: ${result['predicted_price']:,}")
            st.info(f"Estimated Range: ${result['min_estimate']:,} - ${result['max_estimate']:,}")
        else:
            st.error(f"Prediction failed. Status: {res.status_code}")
    except Exception as e:
        st.error(f"Failed to connect to the API. Error: {e}")

