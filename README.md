# 📊 Mutual Fund Analytics

## Bluestock Fintech Capstone Project

A comprehensive end-to-end Data Analytics project focused on Mutual Fund performance, NAV analysis, investor behaviour, portfolio analytics, and risk metrics using **Python, SQL, SQLite, Power BI, and Pandas**.

---

# Project Overview

This project follows a complete Data Analytics workflow from raw data ingestion to interactive dashboard development.

The project includes:

- ETL Pipeline
- Data Cleaning & Validation
- SQLite Database Design
- SQL Analytics
- Exploratory Data Analysis (EDA)
- Performance Analytics
- Advanced Risk Analytics
- Interactive Power BI Dashboard
- Final Reporting

---

# Project Workflow

```
Raw Data
     │
     ▼
ETL Pipeline
     │
     ▼
Data Cleaning
     │
     ▼
SQLite Database
     │
     ▼
SQL Analysis
     │
     ▼
EDA & Performance Analytics
     │
     ▼
Advanced Analytics
     │
     ▼
Power BI Dashboard
     │
     ▼
Final Report
```

---

# Project Structure

```
Mutual_Fund_Analytics/
│
├── data/
│   ├── raw/
│   ├── processed/
│   └── db/
│       └── bluestock_mf.db
│
├── notebooks/
│   ├── 03_eda_analysis.ipynb
│   ├── 04_performance_analytics.ipynb
│   └── 05_advanced_analytics.ipynb
│
├── scripts/
│   ├── etl_pipeline.py
│   ├── data_cleaning.py
│   ├── compute_metrics.py
│   ├── live_nav_fetch.py
│   └── recommender.py
│
├── sql/
│   ├── schema.sql
│   └── queries.sql
│
├── dashboard/
│   └── Mutual_Fund_Analytics_Dashboard.pbix
│
├── reports/
│
├── README.md
└── requirements.txt
```

---

# Technologies Used

- Python
- Pandas
- NumPy
- SQLite
- SQLAlchemy
- SQL
- Requests
- Power BI
- Git
- GitHub

---

# Project Deliverables

## D1 — ETL Pipeline

✔ Automated ETL Pipeline

- Data Loading
- Data Validation
- Missing Value Detection
- Data Quality Checks
- Error Handling

Script:

```
scripts/etl_pipeline.py
```

---

## D2 — SQLite Database

Created SQLite database with proper schema.

Includes:

- NAV History
- Fund Performance
- Investor Transactions

Files

```
data/db/bluestock_mf.db
sql/schema.sql
sql/queries.sql
```

---

## D3 — Exploratory Data Analysis

Performed detailed EDA including

- Missing Values
- Distribution Analysis
- Category Analysis
- NAV Trends
- AUM Analysis
- Investor Behaviour

Notebook

```
notebooks/03_eda_analysis.ipynb
```

---

## D4 — Performance Analytics

Calculated financial metrics including

- CAGR
- Rolling Returns
- Sharpe Ratio
- Alpha
- Beta
- Benchmark Comparison

Outputs

- CSV Reports
- Charts
- Performance Metrics

Notebook

```
notebooks/04_performance_analytics.ipynb
```

---

## D5 — Interactive Dashboard

Developed Power BI Dashboard consisting of four pages.

### Dashboard Pages

- Industry Overview
- Fund Performance
- Investor Analytics
- SIP Market Trends

Features

- Interactive Filters
- KPI Cards
- Slicers
- Drill-down Analysis
- Dynamic Visualizations

---

## D6 — Advanced Analytics

Implemented advanced analytics including

- Value at Risk (VaR)
- Conditional VaR
- Cohort Analysis
- Sector HHI Analysis
- Rolling Sharpe Ratio
- Mutual Fund Recommendation Logic

Notebook

```
notebooks/05_advanced_analytics.ipynb
```

---

# Reports Generated

Generated reports include

- Alpha Beta Analysis
- Benchmark Comparison
- Cohort Analysis
- Fund Scorecard
- Rolling Sharpe Ratio
- Sector Concentration (HHI)
- SIP Continuity Analysis
- Top 10 Funds
- Value at Risk (VaR)

---

# Dashboard Features

✔ Interactive Slicers

✔ KPI Cards

✔ Trend Analysis

✔ Fund Comparison

✔ Investor Insights

✔ SIP Analysis

✔ Performance Metrics

✔ Professional Theme

---

# Key Features

- End-to-End Data Analytics Project
- Automated ETL Pipeline
- Clean Data Processing
- SQLite Database
- SQL Analytics
- Exploratory Data Analysis
- Financial Performance Metrics
- Risk Analytics
- Interactive Dashboard
- Business Insights

---

# Future Improvements

Possible future enhancements include

- Streamlit Web Application
- Automated NAV Scheduler
- Monte Carlo Simulation
- Portfolio Optimisation
- Email Report Automation

---

# Requirements

Install dependencies

```bash
pip install -r requirements.txt
```

---

# Author

**Ashutosh Giri**

B.Tech Artificial Intelligence & Data Science

University School of Automation & Robotics

Guru Gobind Singh Indraprastha University (GGSIPU)

Bluestock Fintech Data Analyst Internship — 2026

---

# License

This project was developed for educational and internship purposes under the Bluestock Fintech Data Analyst Internship Program.