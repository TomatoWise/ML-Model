import streamlit as st
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier
import joblib
# Set the page configuration
st.set_page_config(
    page_title="Fertilizer Recommender",
    page_icon="🌱",
    layout="centered",
)
st.markdown(
    """
    <style>
    .css-3p7mub {
        background-color: #f9f9f9;  /* Cream */
    }
    .css-1v8g2vv {
        background-color: #a6c0e2;  /* Light Blue */
    }
    .css-1i0ljje {
        background-color: #d8d8d8;  /* Grey */
    }
    </style>
    """,
    unsafe_allow_html=True
)
# Load the dataset
data = pd.read_csv("datasets/Fertilizer Prediction.csv")

# Define a function to predict fertilizer
def predict_fertilizer(temperature, humidity, moisture, soil_type, crop_type, nitrogen, potassium, phosphorous):
    # Label encoding for categorical features
    soil_type_enc = le_soil.transform([soil_type])[0]
    crop_type_enc = le_crop.transform([crop_type])[0]
    
    # Create user input data
    user_input = [[temperature, humidity, moisture, soil_type_enc, crop_type_enc, nitrogen, potassium, phosphorous]]
    
    # Predict the fertilizer
    fertilizer_name = model.predict(user_input)
    return fertilizer_name[0]

# Label encoding for categorical features
le_soil = LabelEncoder()
le_crop = LabelEncoder()

# Fit the LabelEncoders with your dataset
le_soil.fit(data['Soil Type'])
le_crop.fit(data['Crop Type'])

# Load the trained model
model = joblib.load("Fertilizer.pkl")

# Create a Streamlit web app
st.title("Fertilizer Recommender")

# Input fields
temperature = st.slider("Temperature", min_value=0, max_value=100)
humidity = st.slider("Humidity", min_value=0, max_value=100)
moisture = st.slider("Moisture", min_value=0, max_value=100)
soil_type = st.selectbox("Soil Type", le_soil.classes_)
crop_type = st.selectbox("Crop Type", le_crop.classes_)
nitrogen = st.slider("Nitrogen Level", min_value=0, max_value=100)
potassium = st.slider("Potassium Level", min_value=0, max_value=100)
phosphorous = st.slider("Phosphorous Level", min_value=0, max_value=100)

if st.button("Predict"):
    result = predict_fertilizer(temperature, humidity, moisture, soil_type, crop_type, nitrogen, potassium, phosphorous)
    st.success(f"Recommended Fertilizer: {result}")
