# 🏥 Obesity Predictor 🍏

[![GitHub License](https://img.shields.io/github/license/VISHWAS304/Obesity-Predictor)](LICENSE)  
[![GitHub Stars](https://img.shields.io/github/stars/vishwas304/Obesity-Predictor)](https://github.com/VISHWAS304/Obesity-Predictor/stargazers)  
[![GitHub Forks](https://img.shields.io/github/forks/vishwas304/Obesity-Predictor)](https://github.com/VISHWAS304/Obesity-Predictor/network/members)

---

## Table of Contents

- [Overview](#overview)
- [Installation & Setup](#installation--setup)
- [Running the Application](#running-the-application)
- [Roadmap](#roadmap)
- [Tech Stack & Implementation](#tech-stack--implementation)
- [Contributing](#contributing)
- [Author](#author)
- [License](#license)
- [Support](#support)

---

## Overview

**Obesity Predictor** is a machine learning web application that forecasts future obesity levels based on user lifestyle inputs. Built with modern MLOps practices, the project is designed for scalability and continuous improvement. This repository documents the current implementation along with a roadmap for future enhancements using additional industry-standard tools.


## Installation & Setup

### Prerequisites
- **Python 3.7+**
- **Docker**
- **AWS Account** (for AWS S3, Glue, RDS, ECR, EC2)
- **Git**

### Setup Steps

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/VISHWAS304/Obesity-Predictor.git
   cd Obesity-Predictor


## Running the Application

### Using Streamlit (Local)

1. **Start the Application:**
   ```bash
   streamlit run app.py
```
  Access the App:
Open your browser at http://localhost:8501.

Using Docker
Build the Docker Image:
```bash
docker build -t obesity-predictor .
```
Run the Docker Container:
```bash
docker run -p 8501:8501 obesity-predictor
```
Access the App:
```bash
Open your browser at http://localhost:8501.
```

```bash
## Roadmap

- **Enhanced Models:** Integrate deep learning with TensorFlow or PyTorch.
- **Experiment Tracking:** Implement MLflow and Weights & Biases for robust tracking.
- **CI/CD Automation:** Develop pipelines using GitHub Actions or Jenkins.
- **Comprehensive Monitoring:** Deploy ELK Stack and Prometheus-Grafana for real-time insights.
- **Workflow Automation:** Use Apache Airflow and Terraform for orchestration and Infrastructure as Code (IaC).

---
---

## Tech Stack & Implementation

### 1. Data Management & Versioning
- **Current:**
  - **[AWS S3](https://aws.amazon.com/s3/)** – Raw data storage  
  - **[AWS Glue](https://aws.amazon.com/glue/)** – ETL operations  
  - **[AWS RDS](https://aws.amazon.com/rds/)** – Structured data storage
- **Planned:**
  - **[Apache Kafka](https://kafka.apache.org/)** / **[NiFi](https://nifi.apache.org/)** – Real-time streaming  
  - **[Delta Lake](https://delta.io/)** – Scalable warehousing  
  - **[DVC](https://dvc.org/)** – Dataset versioning  
  - **[Labelbox](https://labelbox.com/)** – Data labeling

### 2. Model Development & Experimentation
- **Current:**
  - **Python** with **[scikit-learn](https://scikit-learn.org/)** for ML models  
  - Manual experiment tracking
- **Planned:**
  - **[TensorFlow](https://www.tensorflow.org/)** / **[PyTorch](https://pytorch.org/)** – Deep learning integration  
  - **[MLflow](https://mlflow.org/)**, **[Weights & Biases](https://wandb.ai/)** – Advanced experiment tracking

### 3. Model Deployment & Serving
- **Current:**
  - **[Streamlit](https://streamlit.io/)** – UI and API endpoints  
  - **[Docker](https://www.docker.com/)** – Containerization  
  - **[AWS EC2](https://aws.amazon.com/ec2/)** & **[ECR](https://aws.amazon.com/ecr/)** – Cloud hosting
- **Planned:**
  - **[FastAPI](https://fastapi.tiangolo.com/)** / **[Flask](https://flask.palletsprojects.com/)** – Production-grade APIs  
  - **[Kubernetes](https://kubernetes.io/)** – Container orchestration  
  - CI/CD with **[GitHub Actions](https://github.com/features/actions)** / **[Jenkins](https://www.jenkins.io/)**

### 4. Monitoring & Automation
- **Current:**
  - Basic logging in Streamlit
- **Planned:**
  - **[ELK Stack](https://www.elastic.co/elk-stack)** / **[Splunk](https://www.splunk.com/)** – Logging & analytics  
  - **[Prometheus](https://prometheus.io/)** / **[Grafana](https://grafana.com/)** – Monitoring  
  - Workflow automation with **[Apache Airflow](https://airflow.apache.org/)**  
  - IaC with **[Terraform](https://www.terraform.io/)**

### 5. Collaboration & Governance
- **Current:**
  - **[Git](https://git-scm.com/)** (via **[GitHub](https://github.com/)**) for code versioning
- **Planned:**
  - **[DVC](https://dvc.org/)** – Dataset versioning  
  - **[HashiCorp Vault](https://www.vaultproject.io/)** – Secure secret management  
  - **[MLflow Model Registry](https://mlflow.org/docs/latest/model-registry.html)** – Model governance

---

## Contributing

Contributions, suggestions, and improvements are welcome. To contribute:

1. **Fork the repository.**
2. Create a new branch for your feature/bug fix.
3. Commit and push your changes.
4. Open a pull request with detailed explanations.

For major changes, please open an issue to discuss before proceeding.

---

## Author

**Vishwas Bhushan Basuru**  
- Email: vishwasbhushanb@gmail.com  
- GitHub: [VISHWAS304](https://github.com/VISHWAS304)

---

## License

This project is licensed under the terms of the [LICENSE](LICENSE) file.

---

## Support

If you find this project useful, please ⭐️ **star** the repository and share it with others!
