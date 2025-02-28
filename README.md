# 🏥 Obesity Predictor 🍏

[![GitHub license](https://img.shields.io/github/license/VISHWAS304/Obesity-Predictor)](LICENSE)  
[![GitHub stars](https://img.shields.io/github/stars/vishwas304/Obesity-Predictor)](https://github.com/vishwas304/Obesity-Predictor/stargazers)  
[![GitHub forks](https://img.shields.io/github/forks/vishwas304/Obesity-Predictor)](https://github.com/vishwas304/Obesity-Predictor/network/members)  

---

## Overview

**Obesity Predictor** is a machine learning-powered web application that predicts future obesity levels based on user lifestyle inputs. Built with Python, Streamlit, and AWS, this repository serves as both a research project and a study resource in Machine Learning and Generative AI.

*Note: While this project uses a selected set of tools and processes to deliver its functionality, additional industry-standard tools and MLOps processes are not implemented in the current version but are considered for future enhancements.*

---

## Features

- **Machine Learning-Powered Predictions:**  
  Uses various ML algorithms to forecast obesity levels based on input data.

- **Interactive Web Application:**  
  A user-friendly interface built with Streamlit for real-time user interaction.

- **Cloud-Integrated Data Handling:**  
  Leverages AWS services (S3, Glue, RDS, ECR, EC2) for storage, ETL, and deployment.

- **Containerized Deployment:**  
  Docker is used for building and deploying the application, ensuring consistency across environments.

- **SQL & Generative AI Integration:**  
  Implements SQL along with LLMs for natural language interaction with the database.

---

## Tech Stack

- **Programming Language:** Python  
  - OOP & Modular Coding  
  - Streamlit for building the API and user interface

- **Database & SQL:**  
  - SQL integrated with Generative AI for natural language querying

- **Machine Learning:**  
  - Various ML algorithms for prediction tasks

- **Containerization:**  
  - Docker for environment consistency and streamlined deployment

- **Cloud Services (AWS Free Tier):**  
  - **AWS S3:** Storage for raw data  
  - **AWS Glue:** ETL operations  
  - **AWS RDS:** Data warehousing  
  - **AWS ECR:** Docker container storage  
  - **AWS EC2:** Cloud deployment  
  - **Streamlit Deployment:** Hosting on the free tier

*Future implementations may integrate additional industry tools such as MLflow for experiment tracking, DVC for data versioning, Apache Kafka for real-time data streaming, Airflow for workflow orchestration, and Kubernetes for container orchestration.*

---

## Getting Started

### Prerequisites

- **Python 3.7+**
- **Docker**
- **AWS Account** (for AWS S3, Glue, RDS, ECR, and EC2 services)
- **Git**
