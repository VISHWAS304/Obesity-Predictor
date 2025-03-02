import streamlit as st
import pandas as pd
import pickle
import json
from pathlib import Path

# -----------------------------------------------------------------------------
# 1. Set up Streamlit configuration
# -----------------------------------------------------------------------------
st.set_page_config(
    page_title="Obesity Level Predictor",
    page_icon="🍏",
    layout="wide"
)

# Load the external CSS file
with open("styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# 2. Header Section (Logo + Title)
# -----------------------------------------------------------------------------
with st.container():
    col1, col2, col3 = st.columns([1, 3, 1])
    st.markdown(
        """
        <div class="header-container">
            <h1 class="title">Future Obesity Level Predictor</h1>
            <p class="subtext">Predict your future obesity level based on your lifestyle habits.</p>
            <hr>
        </div>
        """,
        unsafe_allow_html=True
    )

# -----------------------------------------------------------------------------
# 3. Sidebar (Model Selection & Database Settings)
# -----------------------------------------------------------------------------
st.sidebar.image("images/obesity.png", width=150)

st.sidebar.header("⚙️ Model Selection")
model_choice = st.sidebar.radio("Select a model:", ("Logistic Regression", "Decision Tree"))
st.sidebar.markdown("<hr>", unsafe_allow_html=True)

st.sidebar.subheader("Database Settings")
host = st.sidebar.text_input("Host", value="localhost")
port = st.sidebar.text_input("Port", value="3306")
user = st.sidebar.text_input("User", value="root")
password = st.sidebar.text_input("Password", type="password", value="")
database = st.sidebar.text_input("Database", value="obesity_predictor")

if st.sidebar.button("Connect"):
    with st.spinner("Connecting to database..."):
        # Placeholder for your actual database connection function
        st.success("Connected to database!")
        st.session_state.db = "Your connection object"  # Placeholder

# -----------------------------------------------------------------------------
# 4. User Inputs (Form with Expanders)
# -----------------------------------------------------------------------------
st.subheader("📝 Enter Your Details")
st.markdown("###### Click each section to expand and fill in the details.")

with st.form(key="user_details_form"):
    # Personal Information Section
    with st.expander("👤 Personal Information", expanded=False):
        gender = st.selectbox("🚻 Gender", ["Male", "Female"])
        age = st.number_input("📅 Age", min_value=10, max_value=100, step=1)
        height = st.number_input("📏 Height (m)", min_value=1.0, max_value=2.5, step=0.01)
        weight = st.number_input("⚖️ Weight (kg)", min_value=20, max_value=200, step=1)
        family_history = st.selectbox("👨‍👩‍👧‍👦 Family History of Overweight?", ["Yes", "No"])
    
    # Dietary Information Section
    with st.expander("🥗 Dietary Information", expanded=False):
        fcvc = st.selectbox("🥦 Vegetable Consumption?", ["Rarely", "Sometimes", "Frequently"])
        ncp = st.number_input("🍽️ Number of Main Meals per Day", min_value=1, max_value=6, step=1)
        favc = st.selectbox("🍔 High Caloric Food Consumption?", ["Yes", "No"])
        caec = st.selectbox("🍪 Eating Between Meals?", ["No", "Sometimes", "Frequently", "Always"])
    
    # Lifestyle Information Section
    with st.expander("🏋️ Lifestyle Information", expanded=False):
        smoke = st.selectbox("🚬 Do You Smoke?", ["Yes", "No"])
        ch2o = st.number_input("💧 Water Consumption (Liters per day)", min_value=0.5, max_value=5.0, step=0.1)
        faf = st.selectbox("🏋️ Physical Activity Frequency", ["None", "Low", "Moderate", "High"])
        tue = st.number_input("📱 Time Using Technology (Hours per day)", min_value=0, max_value=24, step=1)
    
    # Centered Predict Button inside the form (styled via external CSS)
    submitted = st.form_submit_button("Predict Future Obesity")

if submitted:
    st.success("✅ Prediction process initiated!")

# -----------------------------------------------------------------------------
# 5. Feature Alignment & Prediction Logic
# -----------------------------------------------------------------------------
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

def align_features(input_data):
    """Ensure user input data matches the training feature set."""
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

if submitted:
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
    
    if aligned_input is not None:
        try:
            aligned_input.fillna(0, inplace=True)
            with open(MODEL_PATHS[model_choice], "rb") as f:
                model = pickle.load(f)
            prediction = model.predict(aligned_input)[0]
            obesity_label = OBESITY_CLASS_MAPPING.get(prediction, "Unknown")
            
            # Map prediction to CSS classes defined in styles.css
            card_classes = {
                0: "card-underweight",
                1: "card-normal",
                2: "card-overweight",
                3: "card-obesity-type1",
                4: "card-obesity-type2",
                5: "card-obesity-type3"
            }
            card_class = card_classes.get(prediction, "card-default")
            
            st.markdown(
                f"""
                <div class="{card_class}">
                    <h2>{obesity_label}</h2>
                    <p class="card-text">
                        Please note that this prediction is only an initial observation and should not be considered definitive.
                        For a comprehensive evaluation, please consult a qualified healthcare professional.
                    </p>
                </div>
                """,
                unsafe_allow_html=True
            )
        except Exception as e:
            st.error(f"Prediction Error: {str(e)}")

# -----------------------------------------------------------------------------
# 6. Footer & Developer Tools
# -----------------------------------------------------------------------------
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown(
    """
    <div class="footer">
        Stay motivated and keep pushing your limits! 🌟 🌱 💪
    </div>
    """,
    unsafe_allow_html=True
)

# Developer Tools Access
st.markdown("<hr>", unsafe_allow_html=True)
st.subheader("Developer Tools Access")
st.markdown(
    "💻 **Please enter your query in natural language if you have database access.** "
    "This feature is intended for developers and owners only."
)
dev_query = st.text_input("Database Query", help="Type your query in natural language to interact with the database.")

if dev_query and dev_query.strip():
    if "db" in st.session_state:
        try:
            response = "Simulated response based on your query."
            st.write(f"**Query:** {dev_query}")
            st.write(f"**Response:** {response}")
        except Exception as e:
            st.error(f"Failed to process the query: {str(e)}")
    else:
        st.error("🚫 Database connection not established. Please connect to the database first.")

with st.expander("Need help with queries?"):
    st.markdown(
        """
        Here are some tips for writing effective SQL queries:
        - Use **SELECT** to specify the columns you want to retrieve.
        - Use **FROM** to specify the tables from which to retrieve data.
        - Use **WHERE** to specify any conditions for the data.
        - Ensure your queries are correctly formatted and your database permissions are set appropriately.
        """
    )

# -----------------------------------------------------------------------------
# 7. Developer Information
# -----------------------------------------------------------------------------
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown(
    """
    <div style="background-color: #ffffff; border: 1px solid #e0e0e0; border-radius: 10px; padding: 20px; 
                box-shadow: 0 4px 12px rgba(0,0,0,0.1); max-width: 600px; margin: 20px auto;">
        <h2 style="text-align: center; color: #003366; margin-bottom: 10px;">Contact for Collaboration</h2>
        <hr style="border-top: 2px solid #e0e0e0; width: 80%; margin: auto;">
        <div style="font-size: 16px; color: #333; margin-top: 20px;">
            <p><strong>Name:</strong> Vishwas Bhushan Basuru</p>
            <p><strong>Role:</strong> ML / AI Engineer</p>
            <p><strong>Contact:</strong> 5519989619</p>
            <p><strong>Email:</strong> <a href="mailto:vishwasbhushanb@gmail.com" style="color: #1e90ff;">vishwasbhushanb@gmail.com</a></p>
            <p><strong>Location:</strong> New York</p>
            <p><strong>External Links:</strong></p>
            <div style="display: flex; justify-content: center; align-items: center; gap: 20px; margin-top: 10px;">
                <a href="https://www.linkedin.com/in/vishwas-bhushan-basuru-819723260/" target="_blank" style="text-decoration: none; color: #1e90ff;">
                    <img src="https://cdn-icons-png.flaticon.com/512/174/174857.png" alt="LinkedIn" style="width: 32px; height: 32px; vertical-align: middle; margin-right: 5px;">LinkedIn
                </a>
                <a href="https://medium.com/@vishwasbhushanb" target="_blank" style="text-decoration: none; color: #1e90ff;">
                    <img src="https://cdn-icons-png.flaticon.com/512/2111/2111505.png" alt="Medium" style="width: 32px; height: 32px; vertical-align: middle; margin-right: 5px;">Medium
                </a>
                <a href="https://github.com/VISHWAS304" target="_blank" style="text-decoration: none; color: #1e90ff;">
                    <img src="https://cdn-icons-png.flaticon.com/512/25/25231.png" alt="GitHub" style="width: 32px; height: 32px; vertical-align: middle; margin-right: 5px;">GitHub
                </a>
            </div>
            <div style="text-align: center; margin-top: 20px;">
                <a href="https://docs.google.com/forms/d/e/1FAIpQLSfEg5HkUydz-Z_HkaEAs3Wj7NN6MV14wDStsZ4tECNRqsgrww/viewform?usp=dialog" 
                   target="_blank" style="display: inline-block; padding: 10px 20px; background-color: #1e90ff; color: #fff; border-radius: 5px; text-decoration: none; font-weight: bold;">
                    Fill Out Collaboration Form
                </a>
            </div>
        </div>
        <p style="text-align: center; font-size: 14px; color: #777; margin-top: 20px;">
            © Vishwas Bhushan Basuru. All rights reserved.
        </p>
    </div>
    """,
    unsafe_allow_html=True
)