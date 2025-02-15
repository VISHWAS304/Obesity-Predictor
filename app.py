import streamlit as st
import pandas as pd
import pickle
import json
from pathlib import Path

# 📌 Load Model Paths
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

# 🌟 Streamlit UI Configuration (Wide layout to reduce scrolling)
st.set_page_config(
    page_title="Obesity Predictor",
    page_icon="🍏",
    layout="wide",
)

# 🌈 Custom Styling for a **Beautiful, Scroll-Free UI**
st.markdown(
    """
    <style>
        body { font-family: 'Arial', sans-serif; }
        .title { font-size: 36px; font-weight: bold; color: #2c3e50; text-align: center; }
        .subtext { font-size: 20px; text-align: center; color: gray; }
        .stButton>button { background-color: #2c3e50; color: white; font-size: 18px; border-radius: 8px; width: 100%; }
        .stButton>button:hover { background-color: #34495e; }
        .sidebar .sidebar-content { background-color: #ecf0f1; }
        .stRadio { font-size: 16px; }
        .stTabs { font-size: 18px; }
    </style>
    """,
    unsafe_allow_html=True
)

# 📌 Header Section (Centered)
st.markdown("<div class='title'>Obesity Level Predictor 🍏</div>", unsafe_allow_html=True)
st.markdown("<div class='subtext'>Predict your obesity level based on your lifestyle habits.</div>", unsafe_allow_html=True)

# 🎛️ **Sidebar for Model Selection**
st.sidebar.image("images/obesity.png", use_container_width=True)
st.sidebar.header("⚙️ Model Selection")
model_choice = st.sidebar.radio("Select a model:", ("Logistic Regression", "Decision Tree"))

# 📋 **Inputs Organized into Tabs to Reduce Clutter**
tabs = st.tabs(["🏠 Basic Info", "🍽️ Diet & Activity", "🚗 Lifestyle"])

with tabs[0]:  # Basic Info
    col1, col2 = st.columns(2)
    with col1:
        gender = st.selectbox("🚻 Gender", ["Male", "Female"])
        age = st.number_input("📅 Age", min_value=10, max_value=100, step=1)
        height = st.number_input("📏 Height (m)", min_value=1.0, max_value=2.5, step=0.01)
    with col2:
        weight = st.number_input("⚖️ Weight (kg)", min_value=20, max_value=200, step=1)
        family_history = st.selectbox("👨‍👩‍👧‍👦 Family History of Overweight?", ["Yes", "No"])
        favc = st.selectbox("🍔 High Caloric Food Consumption?", ["Yes", "No"])

with tabs[1]:  # Diet & Activity
    col1, col2 = st.columns(2)
    with col1:
        fcvc = st.selectbox("🥦 Vegetable Consumption?", ["Rarely", "Sometimes", "Frequently"])
        ncp = st.number_input("🍽️ Number of Meals Per Day", min_value=1, max_value=6, step=1)
        ch2o = st.number_input("💧 Water Intake (L/day)", min_value=0.5, max_value=5.0, step=0.1)
    with col2:
        faf = st.selectbox("🏋️ Physical Activity", ["None", "Low", "Moderate", "High"])
        tue = st.number_input("📱 Time Using Technology (hrs/day)", min_value=0, max_value=24, step=1)
        caec = st.selectbox("🍪 Eating Between Meals?", ["No", "Sometimes", "Frequently", "Always"])

with tabs[2]:  # Lifestyle
    col1, col2 = st.columns(2)
    with col1:
        smoke = st.selectbox("🚬 Do You Smoke?", ["Yes", "No"])
        scc = st.selectbox("📊 Do You Monitor Calories?", ["Yes", "No"])
    with col2:
        calc = st.selectbox("🍷 Alcohol Consumption?", ["Never", "Sometimes", "Frequently", "Always"])
        mtrans = st.selectbox("🚗 Mode of Transportation", ["Walking", "Bike", "Public Transport", "Car", "Motorbike"])

# **🔹 Function to Align Features**
def align_features(input_data):
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
            aligned_input.fillna(0, inplace=True)

            with open(MODEL_PATHS[model_choice], "rb") as f:
                model = pickle.load(f)

            prediction = model.predict(aligned_input)[0]
            obesity_label = OBESITY_CLASS_MAPPING.get(prediction, "Unknown")

            st.success(f"✅ **Predicted Future Obesity Level: {obesity_label}**")
        except Exception as e:
            st.error(f"Prediction Error: {str(e)}")

# 🏥 **Health Advisory**
st.info("⚠️ **This is just a guideline.** Consult a healthcare professional for personalized advice.")

# 📌 **Footer with Motivational Image**
st.markdown("---")
st.image("images/healthy.jpg", use_container_width=True)
st.markdown("<div style='text-align: center; font-size: 18px;'>🌟 Maintain a healthy lifestyle! 🌱💪</div>", unsafe_allow_html=True)
