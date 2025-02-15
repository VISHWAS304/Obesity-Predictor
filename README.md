
# 🏥 Obesity Predictor 🍏  
[![GitHub license](https://img.shields.io/github/license/vishwas304/Obesity-Predictor)](LICENSE)  
[![GitHub stars](https://img.shields.io/github/stars/vishwas304/Obesity-Predictor)](https://github.com/vishwas304/Obesity-Predictor/stargazers)  
[![GitHub forks](https://img.shields.io/github/forks/vishwas304/Obesity-Predictor)](https://github.com/vishwas304/Obesity-Predictor/network/members)  

🚀 **Obesity Predictor** is a **machine learning-powered web application** that predicts **future obesity levels** based on **user lifestyle inputs**. The system is built using **Python, Streamlit, and AWS** for deployment.  

---

## 📌 Table of Contents  
- [🏗️ Project Structure](#-project-structure)  
- [🛠️ Tech Stack](#️-tech-stack)  
- [🚀 Features](#-features)  
- [💻 Installation & Setup](#-installation--setup)  
- [🚢 Deployment](#-deployment)  
- [⚡ CI/CD Workflow](#-cicd-workflow)  
- [📊 Usage](#-usage)  
- [🚀 Future Improvements](#-future-improvements)  
- [👨‍💻 Author](#-author)  
- [🌟 Support](#-support)  

---

## 🏗️ Project Structure  
📦 Obesity-Predictor
┣ 📂 .github/workflows # CI/CD Pipelines
┣ 📂 config # Configuration Files
┣ 📂 images # UI Assets
┣ 📂 models # Trained Models
┣ 📂 src # Source Code
┣ 📂 templates # Streamlit UI Components
┣ 📜 app.py # Streamlit Application
┣ 📜 Dockerfile # Docker Configuration
┣ 📜 requirements.txt # Dependencies
┣ 📜 README.md # Documentation
---

## 🛠️ Tech Stack  
| Category         | Technologies Used |
|-----------------|-----------------|
| **Frontend**    | Streamlit |
| **Backend**     | Python, FastAPI |
| **ML Models**   | Scikit-Learn, Pickle |
| **Database**    | PostgreSQL / RDS |
| **Deployment**  | AWS (EC2, ECR, ECS), Streamlit |
| **Version Control** | GitHub, GitHub Actions (CI/CD) |
| **Monitoring**  | MLflow, DVC |
| **Containerization** | Docker |

---

## 🚀 Features  
✅ **User-friendly Interface** using **Streamlit**  
✅ **Multiple ML Models** (**Logistic Regression**, **Decision Tree**)  
✅ **Obesity Level Prediction** based on **lifestyle habits**  
✅ **Containerized Deployment** using **Docker & AWS**  
✅ **Fast and Secure** Predictions  

---

## 💻 Installation & Setup  

### 🔧 Prerequisites  
Ensure you have **Python 3.8+**, **Git**, and **Docker** installed.  

### 💻 Local Setup  
```bash
# Clone the repository
git clone https://github.com/vishwas304/Obesity-Predictor.git
cd Obesity-Predictor

# Create and activate a virtual environment
python -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate     # Windows

# Install dependencies
pip install -r requirements.txt

# Run the Streamlit App
streamlit run app.py
🚢 Deployment
🏗️ Deploying on AWS (Docker + ECR + EC2)
✅ 1. Build & Push Docker Image
bash
Copy
Edit
docker build -t obesity-predictor .
aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 920373030142.dkr.ecr.us-east-1.amazonaws.com
docker tag obesity-predictor:latest 920373030142.dkr.ecr.us-east-1.amazonaws.com/obesity-predictor:latest
docker push 920373030142.dkr.ecr.us-east-1.amazonaws.com/obesity-predictor:latest
✅ 2. Run the Container on EC2
bash
Copy
Edit
docker run -d -p 8501:8501 --name obesity-predictor 920373030142.dkr.ecr.us-east-1.amazonaws.com/obesity-predictor:latest
🌐 Deploying on Streamlit
Go to Streamlit Cloud
Click Deploy an App → Connect GitHub Repository
Select the streamlit branch
Set the main file path: app.py
Click Deploy 🎉
⚡ CI/CD Workflow (GitHub Actions)
Workflow Name	Branch	Deployment Target
AWS Deployment	main	EC2 + Docker
Streamlit Deployment	streamlit	Streamlit Cloud
Example AWS Workflow (.github/workflows/aws.yml)

yaml
Copy
Edit
name: AWS Deployment  
on:  
  push:  
    branches:  
      - main  
jobs:  
  deploy:  
    runs-on: ubuntu-latest  
    steps:  
      - name: Checkout Code  
        uses: actions/checkout@v3  

      - name: Build & Push Docker Image  
        run: |
          docker build -t obesity-predictor .
          docker push 920373030142.dkr.ecr.us-east-1.amazonaws.com/obesity-predictor:latest  
📊 Usage
1️⃣ Select a model (Logistic Regression / Decision Tree)
2️⃣ Enter your lifestyle details
3️⃣ Click "Predict" and get results in seconds!


🚀 Future Improvements
✅ Add Neural Network-based Predictions
✅ Improve UI with Custom Styling
✅ Optimize Docker Containers for Faster Deployment
👨‍💻 Author
Vishwas Bhushan
📧 vishwasbhushanb@gmail.com
🔗 GitHub Profile

🌟 Support
If you find this project useful, please ⭐ star the repo! 😊

bash
Copy
Edit
git add .
git commit -m "Updated README"
git push origin main
