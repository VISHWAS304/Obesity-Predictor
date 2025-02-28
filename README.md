# 🏥 Obesity Predictor 🍏

[![GitHub license](https://img.shields.io/github/license/VISHWAS304/Obesity-Predictor)](LICENSE)  
[![GitHub stars](https://img.shields.io/github/stars/vishwas304/Obesity-Predictor)](https://github.com/vishwas304/Obesity-Predictor/stargazers)  
[![GitHub forks](https://img.shields.io/github/forks/vishwas304/Obesity-Predictor)](https://github.com/vishwas304/Obesity-Predictor/network/members)  

---

## Overview

**Obesity Predictor** is a machine learning-powered web application that predicts future obesity levels based on user lifestyle inputs. Built with Python, Streamlit, and AWS, this repository serves as both a research project and a study resource in Machine Learning and Generative AI.

*Note: While the current implementation leverages a selected set of tools and processes, the project is designed with a flexible framework. This allows for the integration of additional industry-standard MLOps tools and practices in future releases.*

---

## MLOps Framework Overview

A robust MLOps strategy ensures that machine learning models are accurate, reliable, scalable, and compliant. The framework is typically divided into the following key areas:

### 1. Data Management & Versioning
- **Data Ingestion & Integration:**  
  Processes for collecting, cleaning, and aggregating data from various sources.  
  *Future tools: Apache Kafka, Apache NiFi, Fivetran, Talend*

- **Data Versioning:**  
  Tracking changes in datasets to ensure consistency and reproducibility.  
  *Future tools: DVC (Data Version Control), Delta Lake*

- **Data Labeling & Annotation:**  
  Organizing and preparing labeled data for supervised learning tasks.  
  *Future tools: Labelbox, SuperAnnotate*

- **Data Quality Assurance:**  
  Techniques to ensure data is accurate, complete, and relevant.

---

### 2. Model Development & Experimentation
- **Model Training & Tuning:**  
  Building models and optimizing hyperparameters.

- **Experiment Tracking:**  
  Logging experiments, configurations, and outcomes to compare different model versions.  
  *Future tools: MLflow, Weights & Biases (W&B), Comet.ml*

- **Reproducibility:**  
  Ensuring that experiments can be reliably repeated with the same results.

---

### 3. Model Deployment & Serving
- **Continuous Integration/Continuous Deployment (CI/CD):**  
  Automating testing, integration, and deployment of ML models.

- **Model Packaging:**  
  Containerization (e.g., Docker) and other techniques for bundling models for deployment.

- **Model Serving:**  
  Deploying models to production environments via APIs or other serving mechanisms.  
  *Future tools: TensorFlow Serving, TorchServe, FastAPI, Flask, AWS SageMaker, Google AI Platform, Azure ML*

---

### 4. Monitoring & Management in Production
- **Model Monitoring:**  
  Continuously tracking model performance, including metrics like latency, throughput, and accuracy.

- **Drift Detection:**  
  Identifying shifts in data distribution or model performance (data drift and concept drift).  
  *Future tools: Evidently AI, Alibi Detect*

- **Logging & Alerting:**  
  Setting up logging for model predictions and automated alerts for anomalies or degradations in performance.  
  *Future tools: ELK Stack (Elasticsearch, Logstash, Kibana), Splunk*

- **Retraining & Continuous Learning:**  
  Pipelines that trigger model retraining when performance drops or new data becomes available.

---

### 5. Pipeline Orchestration & Automation
- **Workflow Management:**  
  Using orchestration tools to automate the ML pipeline.  
  *Future tools: Apache Airflow, Kubeflow Pipelines*

- **Infrastructure as Code (IaC):**  
  Managing infrastructure through code to ensure consistency and repeatability.  
  *Future tools: Terraform, Ansible*

- **Scalability & Resource Management:**  
  Leveraging cloud platforms and container orchestration (e.g., Kubernetes) for scalable deployments.

---

### 6. Collaboration & Governance
- **Version Control:**  
  Using tools (e.g., Git for code and DVC for data) to manage changes and collaborate effectively.

- **Security & Compliance:**  
  Implementing practices to ensure data privacy, secure model access, and regulatory compliance.  
  *Future tools: HashiCorp Vault, data governance platforms like Collibra or Alation*

- **Model Explainability & Fairness:**  
  Techniques to interpret model decisions and ensure that models do not propagate bias.

- **Auditability & Governance:**  
  Maintaining an audit trail of model changes, data lineage, and decision-making processes.  
  *Future tools: MLflow Model Registry, Neptune.ai*

---

## Current Tech Stack

For this project, the following tools and platforms are implemented:

- **Programming Language:** Python  
  - Utilizes Object-Oriented Programming (OOP) and Modular Coding  
  - Streamlit for building both the API and the user interface

- **Cloud Services (AWS Free Tier):**  
  - **AWS S3:** Storage for raw data  
  - **AWS Glue:** ETL operations  
  - **AWS RDS:** Data warehousing  
  - **AWS ECR:** Docker container storage  
  - **AWS EC2:** Cloud deployment  
  - **Streamlit Deployment:** Hosting on the free tier

- **Containerization:**  
  - Docker for building and deploying the application

- **SQL & Generative AI:**  
  - Incorporates SQL for data interactions along with LLM-based approaches for natural language queries

*Future iterations may expand this tech stack to incorporate additional industry-standard tools as outlined in the MLOps framework above.*

---

## Getting Started

### Prerequisites

- **Python 3.7+**
- **Docker**
- **AWS Account** (for AWS S3, Glue, RDS, ECR, and EC2 services)
- **Git**

### Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/VISHWAS304/Obesity-Predictor.git
   cd Obesity-Predictor
