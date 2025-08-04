# Cloud Data Pipeline Monitoring & CI/CD

This project simulates a production-ready cloud-based data pipeline with CI/CD, monitoring, and alerting using AWS-native tools and Jenkins.

## ⚙️ Tech Stack

- **ETL**: AWS Glue (PySpark), Amazon Redshift
- **CI/CD**: Git, Jenkins, Ansible
- **Monitoring & Alerts**: CloudWatch, Lambda, SNS
- **Security & Infra**: IAM roles, S3 Versioning

## 📦 Architecture Overview
             ┌────────────────────┐
             │   Raw Sales Data   │
             │   (CSV in S3)      │
             └─────────┬──────────┘
                       │
                       ▼
             ┌────────────────────┐
             │  AWS Glue Job      │
             │  (PySpark)         │
             └─────────┬──────────┘
                       │
             ┌─────────▼──────────┐
             │ CloudWatch Metrics │
             │ & Log Monitoring   │
             └─────────┬──────────┘
                       │
        ┌──────────────▼──────────────┐
        │      CloudWatch Alarms      │
        └─────────┬──────────┬────────┘
                  │          │
        ┌─────────▼──┐   ┌───▼────────┐
        │ Lambda     │   │ SNS Alerts │
        │ (Failure   │   │ (Email to  │
        │ Handler)   │   │ Data Team) │
        └────────────┘   └────────────┘
                       │
                       ▼
             ┌────────────────────┐
             │ Amazon Redshift    │
             │ (Clean Analytics DB)│
             └────────────────────┘


## 📁 Project Structure
cloud-data-pipeline-monitoring/
│
├── scripts/
│   └── glue_etl_job.py         ← PySpark job for data cleaning & load
│
├── monitoring/
│   └── lambda_handler.py       ← Triggered by CloudWatch on job failure
│
├── jenkins/
│   └── Jenkinsfile             ← CI/CD automation pipeline
│
└── README.md                   ← Documentation & project overview


## ✅ Key Features

- CI/CD pipeline using Jenkins to deploy Glue jobs
- CloudWatch triggers alerts on job failures or delays
- Lambda functions send notifications via SNS
- Redshift as data warehouse target

## 👨‍💼 Author

**Abhinav Rachulapally**  
Data Engineer | AWS | DevOps for Data Pipelines  
[GitHub Profile](https://github.com/abhinavrachulapally)
