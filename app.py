import streamlit as st
import pandas as pd
import pickle
import json
from pathlib import Path

# 📌 Load the saved feature names and models
FEATURES_PATH = Path("config/feature_names.json")
MODEL_PATHS = {
    "Logistic Regression": Path("models/logistic_regression/model.pkl"),
    "Decision Tree": Path("models/decision_tree/model.pkl")
}

OBESITY_CLASS_MAPPING = {
    0: "Underweight 🏃‍♂️",
    1: "Normal Weight ✅",
    2: "Overweight ⚠️",
    3: "Obesity Type I 🚨",
    4: "Obesity Type II ⚠️",
    5: "Obesity Type III 🚨"
}

# 🌟 Streamlit UI Configuration
st.set_page_config(
    page_title="Future Obesity Level Predictor",
    page_icon="🍏",
    layout="wide",
)

# 🌈 Background Styling
st.markdown(
    """
    <style>
        body {
            background-color: #f5f5f5;
            font-family: 'Arial', sans-serif;
        }
        .title {
            font-size: 36px;
            font-weight: bold;
            color: #4CAF50;
            text-align: center;
        }
        .subtext {
            font-size: 20px;
            text-align: center;
            color: gray;
        }
        .stButton>button {
            background-color: #4CAF50;
            color: white;
            font-size: 18px;
            border-radius: 10px;
            width: 100%;
        }
        .stButton>button:hover {
            background-color: #45a049;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# 📌 Header Section
col1, col2, col3 = st.columns([1, 5, 1])
with col2:
    st.image("images/logo.png", width=80)  # Small logo
st.markdown("<div class='title'>Obesity Level Predictor 🍏</div>", unsafe_allow_html=True)
st.markdown("<div class='subtext'>Predict your future obesity level based on your lifestyle habits.</div>", unsafe_allow_html=True)

st.markdown("---")  # Divider

# 🎛️ Sidebar for Model Selection
st.sidebar.image("images/obesity.png", use_container_width=True)
st.sidebar.header("⚙️ Model Selection")
model_choice = st.sidebar.radio("Select a model:", ("Logistic Regression", "Decision Tree"))

# 📋 User Inputs
st.subheader("📝 Enter Your Details")
st.markdown("#### Fill in the details below to predict your obesity level.")

col1, col2 = st.columns(2)
with col1:
    gender = st.selectbox("🚻 Gender", ["Male", "Female"])
    age = st.number_input("📅 Age", min_value=10, max_value=100, step=1)
    height = st.number_input("📏 Height (m)", min_value=1.0, max_value=2.5, step=0.01)
    weight = st.number_input("⚖️ Weight (kg)", min_value=20, max_value=200, step=1)
    family_history = st.selectbox("👨‍👩‍👧‍👦 Family History of Overweight?", ["Yes", "No"])
    favc = st.selectbox("🍔 High Caloric Food Consumption?", ["Yes", "No"])
    fcvc = st.selectbox("🥦 Vegetable Consumption?", ["Rarely", "Sometimes", "Frequently"])
    ncp = st.number_input("🍽️ Number of Main Meals per Day", min_value=1, max_value=6, step=1)

with col2:
    caec = st.selectbox("🍪 Eating Between Meals?", ["No", "Sometimes", "Frequently", "Always"])
    smoke = st.selectbox("🚬 Do You Smoke?", ["Yes", "No"])
    ch2o = st.number_input("💧 Water Consumption (Liters per day)", min_value=0.5, max_value=5.0, step=0.1)
    scc = st.selectbox("📊 Do You Monitor Calories?", ["Yes", "No"])
    faf = st.selectbox("🏋️ Physical Activity Frequency", ["None", "Low", "Moderate", "High"])
    tue = st.number_input("📱 Time Using Technology (Hours per day)", min_value=0, max_value=24, step=1)
    calc = st.selectbox("🍷 Alcohol Consumption?", ["Never", "Sometimes", "Frequently", "Always"])
    mtrans = st.selectbox("🚗 Mode of Transportation", ["Walking", "Bike", "Public Transport", "Car", "Motorbike"])

# **🔹 Function to Align Features**
def align_features(input_data):
    """Ensure user input data matches training feature set."""
    try:
        with open(FEATURES_PATH, "r") as f:
            feature_names = json.load(f)

        aligned_data = pd.DataFrame(columns=feature_names)

        for col in input_data.columns:
            if col in feature_names:
                aligned_data[col] = input_data[col]

        for feature in feature_names:
            if feature not in aligned_data.columns:
                aligned_data[feature] = 0

        return aligned_data
    except Exception as e:
        st.error(f"Feature alignment error: {str(e)}")
        return None

# **🔹 Prepare Data for Prediction**
user_data = {
    "Age": age,
    "BMI": weight / (height ** 2) if height > 0 else 0,
    "FCVC": {"Rarely": 1, "Sometimes": 2, "Frequently": 3}[fcvc],
    "NCP": ncp,
    "CH2O": ch2o,
    "FAF": {"None": 0, "Low": 1, "Moderate": 2, "High": 3}[faf],
    "TUE": tue,
    "Gender_Male": 1 if gender == "Male" else 0,
    "family_history_yes": 1 if family_history == "Yes" else 0,
    "FAVC_yes": 1 if favc == "Yes" else 0
}

input_df = pd.DataFrame([user_data])
aligned_input = align_features(input_df)

if st.button("🔍 Predict Obesity Level"):
    if aligned_input is not None:
        try:
            aligned_input.fillna(0, inplace=True)  # ✅ Replace NaN values with 0 (Modify here)

            with open(MODEL_PATHS[model_choice], "rb") as f:
                model = pickle.load(f)

            prediction = model.predict(aligned_input)[0]
            obesity_label = OBESITY_CLASS_MAPPING.get(prediction, "Unknown")

            st.success(f"✅ Predicted Future Obesity Level: **{obesity_label}**")
        except Exception as e:
            st.error(f"Prediction Error: {str(e)}")

# 🏥 **Health Advisory**
st.info(
    "⚠️ **This is just a guideline.** Ideal weight varies based on factors like muscle mass, body frame, and age. "
    "Always consult a healthcare professional for **personalized advice**."
)

# 📌 **Footer with Motivational Image**
st.markdown("---")
st.image("images/healthy.jpg", use_container_width=True)
st.markdown("<div style='text-align: center; font-size: 18px;'>🌟 Maintain a healthy lifestyle! 🌱💪</div>", unsafe_allow_html=True)
