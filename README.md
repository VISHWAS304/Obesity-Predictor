# 🏥 Obesity Predictor 🍏

[![GitHub License](https://img.shields.io/github/license/VISHWAS304/Obesity-Predictor)](LICENSE)  
[![GitHub Stars](https://img.shields.io/github/stars/vishwas304/Obesity-Predictor)](https://github.com/VISHWAS304/Obesity-Predictor/stargazers)  
[![GitHub Forks](https://img.shields.io/github/forks/vishwas304/Obesity-Predictor)](https://github.com/VISHWAS304/Obesity-Predictor/network/members)  

---

## Overview

**Obesity Predictor** is a machine learning-powered web application that predicts future obesity levels based on user lifestyle inputs. This project is built with modern MLOps practices in mind and is designed for scalability and continuous improvement. The repository details both the current implementation and a roadmap for integrating additional industry-standard tools in the future.

---

## Tech Stack & Implementation

### 1. Data Management & Versioning

- **Data Ingestion & Integration:**
  - **Current:**  
    - **AWS S3** – Storage for raw data used in training and inference.  
    - **AWS Glue** – Executes ETL (Extract, Transform, Load) operations.
  - **Planned Enhancements:**  
    - **Apache Kafka / Apache NiFi** – Real-time data streaming integration.  
    - **Fivetran / Talend** – Automated data ingestion across multiple sources.

- **Data Storage & Warehousing:**
  - **Current:**  
    - **AWS RDS** – Structured database for application data.
  - **Planned Enhancements:**  
    - **Delta Lake** – ACID-compliant data lake for scalable storage.

- **Data Versioning:**
  - **Planned Enhancements:**  
    - **DVC (Data Version Control)** – Track dataset changes alongside code.

- **Data Labeling & Annotation:**
  - **Current:**  
    - Manual processes are used for data labeling.
  - **Planned Enhancements:**  
    - **Labelbox / SuperAnnotate** – Efficient labeling workflows for supervised learning tasks.

---

### 2. Model Development & Experimentation

- **Programming Language & Frameworks:**
  - **Current:**  
    - **Python** – Leveraging object-oriented programming and modular design.  
    - **scikit-learn** – Current machine learning models.
  - **Planned Enhancements:**  
    - **TensorFlow / PyTorch** – Integration for deep learning models.

- **Experiment Tracking:**
  - **Current:**  
    - Manual experiment tracking with standardized code and data management.
  - **Planned Enhancements:**  
    - **MLflow** – Experiment tracking and model registry.  
    - **Weights & Biases (W&B) / Comet.ml** – Advanced experiment tracking and visualization.

- **Reproducibility:**
  - **Current:**  
    - Standardized practices in code and dataset management.
  - **Planned Enhancements:**  
    - Enhanced reproducibility through DVC integration.

---

### 3. Model Deployment & Serving

- **Web Application Framework:**
  - **Current:**  
    - **Streamlit** – Provides the user interface and API endpoints for real-time predictions.
  - **Planned Enhancements:**  
    - **FastAPI / Flask** – Alternative options for production-grade API endpoints.

- **Containerization & Cloud Deployment:**
  - **Current:**  
    - **Docker** – Containerizes the application for consistent environments.  
    - **AWS EC2 & ECR** – Hosts and stores Docker containers in a cloud environment.
  - **Planned Enhancements:**  
    - **Kubernetes** – Orchestrate containerized deployments for scalability.

- **CI/CD Pipelines:**
  - **Current:**  
    - Not yet implemented.
  - **Planned Enhancements:**  
    - **GitHub Actions / Jenkins / GitLab CI** – Automated testing, integration, and deployment pipelines.

- **Model Serving:**
  - **Planned Enhancements:**  
    - **TensorFlow Serving / TorchServe** – Optimized serving for deep learning models.

---

### 4. Monitoring & Management in Production

- **Logging & Monitoring:**
  - **Current:**  
    - Application-level logging integrated within Streamlit.
  - **Planned Enhancements:**  
    - **ELK Stack (Elasticsearch, Logstash, Kibana) / Splunk** – Robust logging and analytics.
    - **Prometheus / Grafana** – Real-time performance monitoring and alerting.

- **Drift Detection & Model Retraining:**
  - **Current:**  
    - No drift detection is implemented.
  - **Planned Enhancements:**  
    - **Evidently AI / Alibi Detect** – Tools to monitor data and concept drift and trigger retraining pipelines.

---

### 5. Pipeline Orchestration & Automation

- **Workflow Management:**
  - **Current:**  
    - Manual execution of scripts.
  - **Planned Enhancements:**  
    - **Apache Airflow / Kubeflow Pipelines** – Automation of complex ML workflows.

- **Infrastructure as Code (IaC):**
  - **Current:**  
    - AWS services are provisioned manually.
  - **Planned Enhancements:**  
    - **Terraform / Ansible** – Automated infrastructure management.

---

### 6. Collaboration & Governance

- **Version Control:**
  - **Current:**  
    - **Git** (hosted on GitHub) for code versioning.
  - **Planned Enhancements:**  
    - **DVC** – Integration for dataset versioning alongside code.

- **Security & Compliance:**
  - **Current:**  
    - AWS IAM roles manage access control.
  - **Planned Enhancements:**  
    - **HashiCorp Vault** – Secure secret management.

- **Auditability & Model Governance:**
  - **Current:**  
    - Manual tracking and governance practices.
  - **Planned Enhancements:**  
    - **MLflow Model Registry / Neptune.ai** – Audit trails and governance for model lifecycle management.

---

## Installation & Setup

### Prerequisites

- Python 3.7 or higher
- Docker
- AWS Account (for AWS S3, Glue, RDS, ECR, and EC2)
- Git

### Installation Steps

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/VISHWAS304/Obesity-Predictor.git
   cd Obesity-Predictor
