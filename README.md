# Mutual Fund Analytics

## Bluestock Fintech Capstone Project

An end-to-end Mutual Fund Analytics project developed as part of the Bluestock Fintech Data Analyst Internship. This project demonstrates the complete Data Analytics lifecycle including data ingestion, cleaning, database design, SQL analytics, exploratory data analysis, Power BI dashboard development, advanced financial analytics, and investor behavior analysis using Python, SQL, SQLite, and Power BI.

---

# Project Overview

The objective of this project is to analyze mutual fund data and generate meaningful business insights related to:

- Mutual Fund Performance
- NAV Trends
- Investor Transactions
- AUM Distribution
- Portfolio Holdings
- SIP Behaviour
- Risk Metrics
- Portfolio Diversification
- Investor Cohort Analysis

The project follows a complete end-to-end analytics workflow from raw data to business intelligence dashboards and advanced financial analysis.

---

# Project Workflow

- Data Ingestion (ETL)
- Data Cleaning & Validation
- SQLite Database Design
- SQL Analytics
- Exploratory Data Analysis (EDA)
- Performance Analytics
- Power BI Dashboard Development
- Advanced Financial Analytics
- Risk Metrics
- Fund Recommendation System
- Documentation & Reporting

---

# Project Structure

```text
Mutual_Fund_Analytics/
│
├── dashboard/
│   └── Mutual_Fund_Analytics_Dashboard.pbix
│
├── data/
│   ├── raw/
│   └── processed/
│
├── notebooks/
│   ├── EDA_Analysis.ipynb
│   ├── Performance_Analytics.ipynb
│   └── Advanced_Analytics.ipynb
│
├── reports/
│   ├── benchmark_comparison.png
│   ├── rolling_sharpe_chart.png
│   ├── top10_funds.png
│   ├── var_cvar_report.csv
│   ├── cohort_analysis.csv
│   ├── sip_continuity_analysis.csv
│   ├── sector_hhi_analysis.csv
│   ├── alpha_beta.csv
│   ├── fund_scorecard.csv
│   └── data_dictionary.md
│
├── sql/
│   ├── schema.sql
│   └── queries.sql
│
├── data_ingestion.py
├── live_nav_fetch.py
├── data_cleaning.py
├── database_load.py
├── recommender.py
├── bluestock_mf.db
├── requirements.txt
└── README.md
```

---

# Project Modules

## 1. Data Ingestion

Completed Tasks

- Created project structure
- Loaded multiple mutual fund datasets
- Explored dataset dimensions
- Checked missing values
- Validated AMFI scheme codes
- Fetched live NAV data using MFAPI
- Generated initial data quality summary

Deliverables

- data_ingestion.py
- live_nav_fetch.py

---

## 2. Data Cleaning & Validation

Completed Tasks

- Removed duplicate records
- Converted date columns
- Validated NAV values
- Cleaned transaction records
- Standardized categorical data
- Generated cleaned datasets

Deliverables

- data_cleaning.py

---

## 3. Database Development

Completed Tasks

- Designed SQLite database
- Loaded cleaned datasets
- Created fact tables
- Implemented relational schema

Database

- SQLite
- SQLAlchemy

Deliverables

- bluestock_mf.db
- schema.sql

---

## 4. SQL Analytics

Implemented analytical SQL queries for:

- Top Funds by AUM
- Average NAV
- Fund Performance
- State-wise Transactions
- SIP Analysis
- Category Analysis
- Gender Analysis
- Risk Grade Distribution
- City-wise Transactions
- Expense Ratio Analysis

Deliverables

- queries.sql

---

## 5. Exploratory Data Analysis (EDA)

Performed:

- NAV Trend Analysis
- Fund Category Analysis
- AUM Analysis
- Portfolio Analysis
- Investor Transaction Analysis
- Benchmark Comparison
- Alpha & Beta Analysis
- Business Insights

Notebook

- EDA_Analysis.ipynb

---

## 6. Performance Analytics

Implemented:

- Fund Performance Comparison
- CAGR Analysis
- Rolling Returns
- Benchmark Comparison
- Fund Ranking
- Top Performing Funds

Notebook

- Performance_Analytics.ipynb

---

## 7. Power BI Dashboard

Designed an interactive Power BI dashboard consisting of four pages:

### Page 1

Industry Overview

### Page 2

Fund Performance

### Page 3

Investor Analytics

### Page 4

SIP Market Trends

Dashboard Deliverables

- Power BI (.pbix)
- Dashboard PDF
- Dashboard Screenshots

---

## 8. Advanced Analytics & Risk Metrics

Implemented:

### Historical VaR (95%) & CVaR

- Downside risk estimation

### Rolling 90-Day Sharpe Ratio

- Risk-adjusted return analysis

### Investor Cohort Analysis

- Investor behaviour by joining year

### SIP Continuity Analysis

- Identification of At-Risk investors

### Fund Recommendation System

- Risk-based mutual fund recommendation

### Sector HHI Concentration Analysis

- Portfolio diversification measurement

Notebook

- Advanced_Analytics.ipynb

Python Script

- recommender.py

---

# Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- SQL
- SQLite
- SQLAlchemy
- Jupyter Notebook
- Power BI
- Requests
- Git
- GitHub
- VS Code

---

# Reports Generated

- Benchmark Comparison
- Rolling Sharpe Chart
- Top 10 Funds
- Alpha Beta Report
- Fund Scorecard
- VaR & CVaR Report
- Investor Cohort Analysis
- SIP Continuity Analysis
- Sector HHI Analysis
- Data Dictionary

---

# Key Business Insights

- Identified high-risk mutual funds using Historical VaR and CVaR.
- Compared funds using Rolling 90-Day Sharpe Ratio.
- Analyzed investor behaviour through Cohort Analysis.
- Detected investors likely to discontinue SIPs.
- Evaluated portfolio diversification using HHI.
- Built a risk-based mutual fund recommendation system.
- Developed an interactive Power BI dashboard for business reporting.

---

# Deliverables

- EDA_Analysis.ipynb
- Performance_Analytics.ipynb
- Advanced_Analytics.ipynb
- recommender.py
- SQLite Database
- SQL Files
- Power BI Dashboard
- Dashboard PDF
- Dashboard Screenshots
- Reports
- README.md

---

# Current Status

**Project Status:** ✅ Completed

This capstone project successfully demonstrates an end-to-end Data Analytics workflow using Python, SQL, SQLite, and Power BI for Mutual Fund Analytics.

---

# Author

**Ashutosh Giri**

B.Tech Artificial Intelligence & Data Science

University School of Automation & Robotics

Guru Gobind Singh Indraprastha University (GGSIPU)

Bluestock Fintech Data Analyst Internship – 2026

---

# Acknowledgement

This project was completed as part of the Bluestock Fintech Data Analyst Internship Capstone Program to gain practical experience in Data Analytics, Financial Analytics, Business Intelligence, SQL, and Power BI.