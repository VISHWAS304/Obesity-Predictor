# 🏥 Obesity Predictor 🍏

[![GitHub License](https://img.shields.io/github/license/VISHWAS304/Obesity-Predictor)](LICENSE)  
[![GitHub Stars](https://img.shields.io/github/stars/vishwas304/Obesity-Predictor)](https://github.com/VISHWAS304/Obesity-Predictor/stargazers)  
[![GitHub Forks](https://img.shields.io/github/forks/vishwas304/Obesity-Predictor)](https://github.com/VISHWAS304/Obesity-Predictor/network/members)

---

## Table of Contents

- [Overview](#overview)
- [Tech Stack & Implementation](#tech-stack--implementation)
  - [1. Data Management & Versioning](#1-data-management--versioning)
  - [2. Model Development & Experimentation](#2-model-development--experimentation)
  - [3. Model Deployment & Serving](#3-model-deployment--serving)
  - [4. Monitoring & Management in Production](#4-monitoring--management-in-production)
  - [5. Pipeline Orchestration & Automation](#5-pipeline-orchestration--automation)
  - [6. Collaboration & Governance](#6-collaboration--governance)
- [Installation & Setup](#installation--setup)
- [Running the Application](#running-the-application)
- [Roadmap & Future Development](#roadmap--future-development)
- [Contributing](#contributing)
- [Author](#author)
- [License](#license)
- [Support](#support)

---

## Overview

**Obesity Predictor** is a machine learning-powered web application that predicts future obesity levels based on user lifestyle inputs. Built with modern MLOps practices in mind, this project is designed for scalability and continuous improvement. The repository documents the current implementation and outlines a roadmap for integrating additional industry-standard tools in the future.

---

## Tech Stack & Implementation

This section details the tools and technologies used in the project, divided into current implementations and planned enhancements. Each tool is linked to its official website for further reference.

### 1. Data Management & Versioning

- **Data Ingestion & Integration:**
  - **Current:**  
    - [AWS S3](https://aws.amazon.com/s3/) – Storage for raw data used in training and inference.  
    - [AWS Glue](https://aws.amazon.com/glue/) – Executes ETL (Extract, Transform, Load) operations.
  - **Planned Enhancements:**  
    - [Apache Kafka](https://kafka.apache.org/) / [Apache NiFi](https://nifi.apache.org/) – For real-time data streaming integration.  
    - [Fivetran](https://www.fivetran.com/) / [Talend](https://www.talend.com/) – For automated data ingestion across multiple sources.

- **Data Storage & Warehousing:**
  - **Current:**  
    - [AWS RDS](https://aws.amazon.com/rds/) – Structured database for application data.
  - **Planned Enhancements:**  
    - [Delta Lake](https://delta.io/) – An ACID-compliant data lake for scalable storage.

- **Data Versioning:**
  - **Planned Enhancements:**  
    - [DVC (Data Version Control)](https://dvc.org/) – To track dataset changes alongside code.

- **Data Labeling & Annotation:**
  - **Current:**  
    - Manual processes are used for data labeling.
  - **Planned Enhancements:**  
    - [Labelbox](https://labelbox.com/) / [SuperAnnotate](https://www.superannotate.com/) – For efficient labeling workflows in supervised learning tasks.

---

### 2. Model Development & Experimentation

- **Programming Language & Frameworks:**
  - **Current:**  
    - **Python** – Leveraging object-oriented programming and modular design.  
    - [scikit-learn](https://scikit-learn.org/) – Used for current machine learning models.
  - **Planned Enhancements:**  
    - [TensorFlow](https://www.tensorflow.org/) / [PyTorch](https://pytorch.org/) – For deep learning model integration.

- **Experiment Tracking:**
  - **Current:**  
    - Manual experiment tracking with standardized code and data management.
  - **Planned Enhancements:**  
    - [MLflow](https://mlflow.org/) – For experiment tracking and model registry.  
    - [Weights & Biases (W&B)](https://wandb.ai/) / [Comet.ml](https://www.comet.ml/) – For advanced experiment tracking and visualization.

- **Reproducibility:**
  - **Current:**  
    - Standardized practices in code and dataset management.
  - **Planned Enhancements:**  
    - Enhanced reproducibility through [DVC](https://dvc.org/) integration.

---

### 3. Model Deployment & Serving

- **Web Application Framework:**
  - **Current:**  
    - [Streamlit](https://streamlit.io/) – Provides the user interface and API endpoints for real-time predictions.
  - **Planned Enhancements:**  
    - [FastAPI](https://fastapi.tiangolo.com/) / [Flask](https://flask.palletsprojects.com/) – For production-grade API endpoints.

- **Containerization & Cloud Deployment:**
  - **Current:**  
    - [Docker](https://www.docker.com/) – Containerizes the application for consistent environments.  
    - [AWS EC2](https://aws.amazon.com/ec2/) & [AWS ECR](https://aws.amazon.com/ecr/) – Hosts and stores Docker containers in the cloud.
  - **Planned Enhancements:**  
    - [Kubernetes](https://kubernetes.io/) – For orchestrating containerized deployments and scaling.

- **CI/CD Pipelines:**
  - **Current:**  
    - Not yet implemented.
  - **Planned Enhancements:**  
    - [GitHub Actions](https://github.com/features/actions) / [Jenkins](https://www.jenkins.io/) / [GitLab CI](https://docs.gitlab.com/ee/ci/) – For automated testing, integration, and deployment.

- **Model Serving:**
  - **Planned Enhancements:**  
    - [TensorFlow Serving](https://www.tensorflow.org/tfx/guide/serving) / [TorchServe](https://github.com/pytorch/serve) – For optimized model serving, especially for deep learning models.

---

### 4. Monitoring & Management in Production

- **Logging & Monitoring:**
  - **Current:**  
    - Application-level logging integrated within Streamlit.
  - **Planned Enhancements:**  
    - [ELK Stack (Elasticsearch, Logstash, Kibana)](https://www.elastic.co/elk-stack) / [Splunk](https://www.splunk.com/) – For robust logging and analytics.
    - [Prometheus](https://prometheus.io/) / [Grafana](https://grafana.com/) – For real-time performance monitoring and alerting.

- **Drift Detection & Model Retraining:**
  - **Current:**  
    - No drift detection is implemented.
  - **Planned Enhancements:**  
    - [Evidently AI](https://evidentlyai.com/) / [Alibi Detect](https://github.com/SeldonIO/alibi-detect) – To monitor data and concept drift and trigger retraining pipelines.

---

### 5. Pipeline Orchestration & Automation

- **Workflow Management:**
  - **Current:**  
    - Manual execution of scripts.
  - **Planned Enhancements:**  
    - [Apache Airflow](https://airflow.apache.org/) / [Kubeflow Pipelines](https://www.kubeflow.org/docs/components/pipelines/) – For automation of complex ML workflows.

- **Infrastructure as Code (IaC):**
  - **Current:**  
    - AWS services are provisioned manually.
  - **Planned Enhancements:**  
    - [Terraform](https://www.terraform.io/) / [Ansible](https://www.ansible.com/) – For automated infrastructure management.

---

### 6. Collaboration & Governance

- **Version Control:**
  - **Current:**  
    - [Git](https://git-scm.com/) (hosted on [GitHub](https://github.com/)) for code versioning.
  - **Planned Enhancements:**  
    - [DVC](https://dvc.org/) – For dataset versioning alongside code.

- **Security & Compliance:**
  - **Current:**  
    - AWS IAM roles for access control.
  - **Planned Enhancements:**  
    - [HashiCorp Vault](https://www.vaultproject.io/) – For secure secret management.

- **Auditability & Model Governance:**
  - **Current:**  
    - Manual tracking and governance practices.
  - **Planned Enhancements:**  
    - [MLflow Model Registry](https://mlflow.org/docs/latest/model-registry.html) / [Neptune.ai](https://neptune.ai/) – For audit trails and governance throughout the model lifecycle.

---

## Installation & Setup

### Prerequisites

- **Python 3.7 or higher**
- **Docker**
- **AWS Account** (for services such as AWS S3, Glue, RDS, ECR, and EC2)
- **Git**

### Installation Steps

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/VISHWAS304/Obesity-Predictor.git
   cd Obesity-Predictor
