# 🏥 Obesity Predictor 🍏

[![GitHub license](https://img.shields.io/github/license/VISHWAS304/Obesity-Predictor)](LICENSE)  
[![GitHub stars](https://img.shields.io/github/stars/vishwas304/Obesity-Predictor)](https://github.com/vishwas304/Obesity-Predictor/stargazers)  
[![GitHub forks](https://img.shields.io/github/forks/vishwas304/Obesity-Predictor)](https://github.com/vishwas304/Obesity-Predictor/network/members)  

---

## Overview

**Obesity Predictor** is a machine learning-powered web application that predicts future obesity levels based on user lifestyle inputs. This project is structured with modern MLOps practices in mind and is continuously evolving with enhanced tools and processes.

*Note: The repository includes both currently implemented tools and future planned tools, which are highlighted in green.*

---

## Tech Stack & Implementation

### 1. Data Management & Versioning
- **Data Ingestion & Integration:**  
  - **AWS S3:** Stores original raw data for training and inference.  
  - **AWS Glue:** Executes ETL (Extract, Transform, Load) operations.

Future Implementation:
  - <span style="color:green;">**Apache Kafka / Apache NiFi:** Future integration for real-time data streaming.</span>
  - <span style="color:green;">**Fivetran / Talend:** Automating data ingestion across multiple sources.</span>

- **Data Storage & Warehousing:**  
  - **AWS RDS:** Serves as the structured database.
 
  Future Implementation:
  - <span style="color:green;">**Delta Lake:** ACID-compliant data lake for scalable storage.</span>

- **Data Versioning:**
  Future Implementation:
  - <span style="color:green;">**DVC (Data Version Control):** Future integration for tracking dataset changes alongside code.</span>

- **Data Labeling & Annotation:**  
  - **Manual process for now.**

    Future Implementation:
  - <span style="color:green;">**Labelbox / SuperAnnotate:** Future enhancement for efficient labeling workflows.</span>

---

### 2. Model Development & Experimentation
- **Programming Language & Frameworks:**  
  - **Python (OOP & Modular Structure)**  
  - **scikit-learn (Current ML models)**
 
    Future Implementation:
  - <span style="color:green;">**TensorFlow / PyTorch:** Future integration for deep learning models.</span>

- **Experiment Tracking:**  
  - **MLflow**

    Future Implementation:
  - <span style="color:green;"> Weights & Biases (W&B) / Comet.ml:** Future tools for experiment tracking and model registry.</span>

- **Reproducibility:**  
  - **Standardized code and dataset management.**
 
    Future Implementation:
  - <span style="color:green;">**DVC integration planned to improve reproducibility.**</span>

---

### 3. Model Deployment & Serving
- **Web Application Framework:**  
  - **Streamlit:** Provides UI and API endpoints for real-time predictions.
 
    Future Implementation:
  - <span style="color:green;">**FastAPI / Flask:** Future alternative for production-grade API endpoints.</span>

- **Containerization & Cloud Deployment:**  
  - **Docker:** Used to containerize the application.  
  - **AWS EC2 & ECR:** Hosts Docker containers in a cloud environment.
 
    Future Implementation: 
  - <span style="color:green;">**Kubernetes:** Future orchestration for containerized deployments.</span>

- **CI/CD Pipelines:**  
  - **Not yet implemented.**
  - <span style="color:green;">**GitHub Actions / Jenkins / GitLab CI:** Future automation for testing and deployment.</span>

- **Model Serving:**  
  - <span style="color:green;">**TensorFlow Serving / TorchServe:** Future enhancement for optimized model deployment.</span>

---

### 4. Monitoring & Management in Production
- **Logging & Basic Monitoring:**  
  - **Application-level logging in Streamlit.**
  - <span style="color:green;">**ELK Stack (Elasticsearch, Logstash, Kibana) / Splunk:** Future robust logging and analytics.</span>

- **Performance Monitoring & Alerts:**  
  - **Currently manual checks.**
  - <span style="color:green;">**Prometheus / Grafana:** Future real-time monitoring and alerting.</span>

- **Drift Detection & Model Retraining:**  
  - **No drift detection implemented yet.**
  - <span style="color:green;">**Evidently AI / Alibi Detect:** Future integration to track data and concept drift.</span>

---

### 5. Pipeline Orchestration & Automation
- **Workflow Management:**  
  - **Currently manual execution of scripts.**
  - <span style="color:green;">**Apache Airflow / Kubeflow Pipelines:** Future automation of complex ML workflows.</span>

- **Infrastructure as Code (IaC):**  
  - **Currently manually provisioned AWS services.**
  - <span style="color:green;">**Terraform / Ansible:** Future automated infrastructure management.</span>

---

### 6. Collaboration & Governance
- **Version Control:**  
  - **Git (GitHub) for code versioning.**
  - <span style="color:green;">**DVC:** Future integration for dataset versioning.</span>

- **Security & Compliance:**  
  - **AWS IAM roles for access control.**
  - <span style="color:green;">**HashiCorp Vault:** Future integration for secure secret management.</span>

- **Auditability & Model Governance:**  
  - **Currently, tracking is manual.**
  - <span style="color:green;">**MLflow Model Registry / Neptune.ai:** Future integration for audit trails and governance.</span>

---

## Installation & Setup

### Prerequisites
- **Python 3.7+**
- **Docker**
- **AWS Account** (for AWS S3, Glue, RDS, ECR, and EC2)
- **Git**

### Installation

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/VISHWAS304/Obesity-Predictor.git
   cd Obesity-Predictor
