# 📊 Mutual Fund Analytics

<div align="center">

## 🚀 Bluestock Fintech Capstone Project I

### End-to-End Mutual Fund Analytics using Python, SQL, SQLite & Power BI

![Python](https://img.shields.io/badge/Python-3.12-blue?style=for-the-badge&logo=python)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458?style=for-the-badge&logo=pandas)
![SQLite](https://img.shields.io/badge/SQLite-Database-003B57?style=for-the-badge&logo=sqlite)
![PowerBI](https://img.shields.io/badge/Power%20BI-Dashboard-F2C811?style=for-the-badge&logo=powerbi)
![GitHub](https://img.shields.io/badge/GitHub-Version%20Control-181717?style=for-the-badge&logo=github)
![Status](https://img.shields.io/badge/Project-Completed-success?style=for-the-badge)
![License](https://img.shields.io/badge/License-Educational-green?style=for-the-badge)

**An End-to-End Financial Analytics & Business Intelligence Solution built during the Bluestock Fintech Data Analyst Internship.**

</div>

---

## 📌 Project Overview

The **Mutual Fund Analytics** project is a comprehensive end-to-end financial analytics solution developed as part of **Bluestock Fintech Capstone Project I**.

The project transforms raw mutual fund datasets into meaningful business intelligence using modern data analytics techniques. It covers the complete workflow from data ingestion and preprocessing to financial performance evaluation, advanced risk analysis, and interactive dashboard development.

This capstone demonstrates practical implementation of **Python, SQL, SQLite, Power BI, and data visualization techniques** to solve real-world investment analysis problems and support data-driven decision-making.

---

# 🎯 Project Objectives

This project was designed with the following objectives:

- Develop an automated ETL pipeline for mutual fund datasets.
- Clean, validate, and preprocess raw financial data.
- Design a normalized SQLite relational database.
- Perform SQL-based business analytics and financial reporting.
- Conduct Exploratory Data Analysis (EDA) to uncover trends and patterns.
- Calculate advanced financial performance metrics including Sharpe Ratio, Alpha, Beta, CAGR, Maximum Drawdown, VaR, and CVaR.
- Build an interactive Power BI dashboard for business intelligence.
- Generate actionable insights to support investment decision-making.

---

# ✨ Key Features

## 📥 Data Engineering

- Automated ETL Pipeline
- Data Cleaning & Validation
- Missing Value Handling
- Duplicate Detection & Removal
- Data Standardization
- Live NAV Integration

---

## 🗄️ Database & SQL

- SQLite Relational Database
- Normalized Database Schema
- Advanced SQL Queries
- Business Analytics
- Performance Reporting

---

## 📊 Analytics

- Exploratory Data Analysis (EDA)
- Financial Performance Analysis
- Risk Analysis
- Portfolio Analytics
- Investor Behaviour Analysis
- Benchmark Comparison

---

## 📈 Advanced Analytics

- Value at Risk (VaR)
- Conditional Value at Risk (CVaR)
- Rolling Sharpe Ratio
- Cohort Analysis
- SIP Continuity Analysis
- Recommendation Engine

---

## 📊 Business Intelligence

- Interactive Power BI Dashboard
- Dynamic KPI Cards
- Interactive Slicers
- Drill-through Analysis
- Professional Dashboard Design
- Business Insights & Recommendations

---

# 🏛️ Project Architecture

The project follows a structured Data Analytics pipeline that transforms raw mutual fund data into actionable business intelligence.

```text
                  Mutual Fund Analytics Pipeline

     Raw Mutual Fund Datasets + Live NAV (MFAPI)
                        │
                        ▼
              ETL Pipeline (Python)
                        │
                        ▼
         Data Cleaning & Validation
                        │
                        ▼
      Processed CSV Files & SQLite Database
                        │
                        ▼
            SQL Business Analytics
                        │
                        ▼
      Exploratory Data Analysis (EDA)
                        │
                        ▼
     Performance & Risk Analytics
                        │
                        ▼
      Advanced Financial Analytics
                        │
                        ▼
     Interactive Power BI Dashboard
                        │
                        ▼
 Business Insights & Investment Recommendations
```

---

# 🔄 Project Workflow

The project is divided into seven major phases.

| Phase | Description |
|--------|-------------|
| 📥 Data Collection | Import Mutual Fund datasets and Live NAV data |
| ⚙️ ETL Pipeline | Clean, validate and preprocess datasets |
| 🗄️ Database Design | Store processed data inside SQLite |
| 📈 Data Analytics | SQL Analysis & Exploratory Data Analysis |
| 📊 Financial Analytics | Performance Metrics & Risk Analysis |
| 📉 Business Intelligence | Interactive Power BI Dashboard |
| 📄 Documentation | Final Report, Presentation & GitHub |

---

# 📂 Project Structure

```text
Mutual_Fund_Analytics
│
├── 📁 data
│   ├── raw
│   ├── processed
│   └── db
│       └── bluestock_mf.db
│
├── 📁 notebooks
│   ├── 01_data_ingestion.ipynb
│   ├── 02_data_cleaning.ipynb
│   ├── 03_eda_analysis.ipynb
│   ├── 04_performance_analytics.ipynb
│   └── 05_advanced_analytics.ipynb
│
├── 📁 scripts
│   ├── etl_pipeline.py
│   ├── data_cleaning.py
│   ├── compute_metrics.py
│   ├── live_nav_fetch.py
│   └── recommender.py
│
├── 📁 sql
│   ├── schema.sql
│   └── queries.sql
│
├── 📁 dashboard
│   └── Mutual_Fund_Analytics_Dashboard.pbix
│
├── 📁 reports
│   ├── Final_Report.pdf
│   ├── Mutual-Fund-Analytics.pptx
│   └── Final_Report.docx
│
├── README.md
└── requirements.txt
```

---

# 🛠️ Technology Stack

| Category | Technologies |
|----------|--------------|
| Programming | Python |
| Data Analysis | Pandas, NumPy |
| Database | SQLite, SQL |
| Visualization | Matplotlib, Power BI |
| IDE | Jupyter Notebook, VS Code |
| Version Control | Git & GitHub |
| API | MFAPI |

# 📊 Dataset Description

The project integrates **10+ mutual fund datasets** along with **Live NAV data** fetched from the MFAPI service. These datasets cover multiple aspects of mutual fund performance, investor behavior, and market trends.

### Datasets Used

| Dataset | Description |
|----------|-------------|
| NAV History | Historical Net Asset Value records |
| Scheme Performance | Fund returns and performance metrics |
| Assets Under Management (AUM) | Fund size across AMCs |
| SIP Inflows | Monthly SIP investment trends |
| Benchmark Data | Market index performance |
| Investor Transactions | Purchase, SIP & redemption records |
| Portfolio Holdings | Fund allocation across sectors |
| Category Information | Equity, Debt, Hybrid classifications |
| Fund House Details | Asset Management Company information |
| Live NAV (MFAPI) | Real-time NAV integration |

---

# ⚙️ ETL Pipeline

A fully automated ETL (Extract, Transform, Load) pipeline was developed using Python to ensure reliable and repeatable data processing.

## ETL Workflow

```text
Extract
   │
   ▼
Validate
   │
   ▼
Clean
   │
   ▼
Transform
   │
   ▼
Standardize
   │
   ▼
Load into SQLite
```

### ETL Features

- Automated dataset loading
- Missing value handling
- Duplicate record removal
- Data type conversion
- Data validation
- Schema standardization
- Error handling
- SQLite integration

### Main Scripts

```text
scripts/
├── etl_pipeline.py
├── data_cleaning.py
├── compute_metrics.py
├── live_nav_fetch.py
└── recommender.py
```

---

# 🗄️ SQLite Database

A normalized SQLite database was designed to efficiently store and manage processed mutual fund data.

### Database Components

- NAV History
- Scheme Performance
- Portfolio Holdings
- Investor Transactions
- Benchmark Data

### SQL Files

```text
sql/
├── schema.sql
└── queries.sql
```

### Database Features

- Normalized schema
- Optimized SQL queries
- Fast data retrieval
- Structured relationships
- Business reporting support

---

# 📈 SQL Analytics

SQL was used to answer important business questions related to mutual fund performance and investor behavior.

### Business Questions Solved

- Which mutual funds generated the highest returns?
- Which fund categories attracted maximum investments?
- How have SIP inflows changed over time?
- Which benchmark indices outperformed?
- Which fund houses manage the highest AUM?
- How is investor behavior distributed across categories?

### SQL Capabilities

- Aggregation
- Window Functions
- Grouping
- Ranking
- Joins
- Common Table Expressions (CTEs)
- Analytical Queries

---

# 📊 Exploratory Data Analysis (EDA)

Exploratory Data Analysis (EDA) was performed to understand data quality, identify hidden trends, analyze investor behavior, and generate actionable business insights.

### Analysis Performed

- Missing Value Analysis
- Duplicate Record Detection
- Category-wise Fund Distribution
- NAV Trend Analysis
- Assets Under Management (AUM) Analysis
- Fund House Comparison
- Portfolio Allocation Analysis
- Investor Demographics
- SIP Trend Analysis
- Benchmark Comparison

### Key Insights

- Equity funds dominated the industry in terms of Assets Under Management (AUM).
- SIP investments showed a consistent upward trend across the study period.
- Large Cap funds demonstrated more stable long-term performance.
- Certain fund houses consistently outperformed the industry benchmark.

Notebook

```text
notebooks/03_eda_analysis.ipynb
```

---

# 📈 Performance Analytics

A comprehensive performance evaluation framework was developed to measure the return, risk, and consistency of each mutual fund.

## Performance Metrics

| Metric | Purpose |
|---------|----------|
| Annual Return | Overall yearly growth |
| CAGR | Long-term annualized growth |
| Rolling Returns | Performance consistency |
| Sharpe Ratio | Risk-adjusted return |
| Sortino Ratio | Downside risk evaluation |
| Alpha | Excess return over benchmark |
| Beta | Market sensitivity |
| Maximum Drawdown | Largest portfolio decline |
| Value at Risk (VaR) | Expected downside risk |
| Conditional VaR (CVaR) | Tail risk estimation |

### Generated Reports

- Performance Scorecard
- Benchmark Comparison
- Alpha-Beta Analysis
- Rolling Return Report
- Sharpe Ratio Report
- Risk Metrics Summary
- Top Performing Funds

Notebook

```text
notebooks/04_performance_analytics.ipynb
```

---

# 📉 Advanced Analytics & Risk Analysis

Advanced financial analytics were implemented to evaluate investment risk, investor behavior, and portfolio diversification.

## Risk Analytics

- Value at Risk (VaR)
- Conditional Value at Risk (CVaR)
- Rolling 90-Day Sharpe Ratio
- Risk-adjusted Performance Analysis

## Investor Analytics

- Investor Cohort Analysis
- SIP Continuity Analysis
- Transaction Behaviour Analysis

## Portfolio Analytics

- Sector Concentration (HHI)
- Diversification Analysis
- Portfolio Risk Evaluation

## Recommendation Engine

A rule-based recommendation engine was developed to identify suitable mutual fund schemes using:

- Risk Profile
- Historical Performance
- Sharpe Ratio
- Alpha & Beta
- Volatility
- Category Preference

Notebook

```text
notebooks/05_advanced_analytics.ipynb
```

---

# 📊 Project Outputs

The project generated multiple analytical reports including:

- Normalized Performance Comparison
- Rolling Sharpe Ratio Analysis
- Benchmark Comparison
- Alpha & Beta Report
- Fund Scorecard
- Top Performing Funds
- Value at Risk Report
- Cohort Analysis
- SIP Continuity Report
- Sector Concentration Report

---

# 📊 Interactive Power BI Dashboard

A professional **4-page interactive Power BI dashboard** was developed to transform complex mutual fund data into intuitive business intelligence. The dashboard enables investors and analysts to explore market trends, evaluate fund performance, and understand investor behaviour using dynamic visualizations and interactive filters.

---

## 📌 Dashboard Overview

| Dashboard Page | Description |
|----------------|-------------|
| 📈 Industry Overview | Industry KPIs, AUM Trends, SIP Inflows, Fund Houses |
| 💹 Fund Performance | Risk vs Return, Benchmark Comparison, Fund Rankings |
| 👥 Investor Analytics | Investor Behaviour, State-wise Analysis, Age Group Insights |
| 📊 SIP & Market Trends | SIP Growth, Category Trends, Market Movement Analysis |

---

## ✨ Dashboard Features

- Interactive KPI Cards
- Dynamic Slicers
- Cross Filtering
- Drill-through Analysis
- Risk vs Return Visualization
- Benchmark Comparison
- Professional Business Layout
- Investor Behaviour Analysis
- Responsive Dashboard Design

---

# 🖼️ Dashboard Preview

> **Replace the placeholders below with screenshots from your Power BI dashboard.**

### 📈 Industry Overview

dashboard/Page_1_Industry_Overview.png

![Industry Overview](images/dashboard_1.png)

---

### 💹 Fund Performance

dashboard/Page_2_Fund_Performance.png

![Fund Performance](images/dashboard_2.png)

---

### 👥 Investor Analytics

dashboard/Page_3_Investor_Analytics.png

![Investor Analytics](images/dashboard_3.png)

---

### 📊 SIP & Market Trends

dashboard/Page_4_SIP_Market_Trends.png

![SIP & Market Trends](images/dashboard_4.png)

---

# 💡 Key Business Insights

The analysis revealed several valuable insights that can support better investment decisions.

### 📈 Investment Trends

- Equity Mutual Funds generated the highest long-term returns.
- SIP inflows showed consistent year-over-year growth.
- Large Cap Funds demonstrated comparatively lower volatility.
- Risk-adjusted performance varied significantly across fund categories.

### 📊 Investor Behaviour

- Younger investors preferred SIP investments over lump sum investments.
- Metropolitan regions contributed the highest transaction volumes.
- Investor participation increased steadily over the observed period.

### 📉 Risk Analysis

- Higher Sharpe Ratio funds consistently outperformed peers.
- VaR and CVaR highlighted downside risk across different categories.
- Diversified portfolios reduced concentration risk.

---

# 🏆 Project Highlights

✅ Automated ETL Pipeline

✅ Normalized SQLite Database

✅ Advanced SQL Analytics

✅ Exploratory Data Analysis

✅ Performance Analytics

✅ Risk Analytics

✅ Mutual Fund Recommendation Engine

✅ Interactive Power BI Dashboard

✅ Professional Technical Documentation

---

# 📦 Final Deliverables

| Deliverable | Status |
|-------------|--------|
| ETL Pipeline | ✅ Completed |
| SQLite Database | ✅ Completed |
| SQL Analytics | ✅ Completed |
| EDA Notebook | ✅ Completed |
| Performance Analytics | ✅ Completed |
| Advanced Analytics | ✅ Completed |
| Power BI Dashboard | ✅ Completed |
| Final Report | ✅ Completed |
| Presentation | ✅ Completed |
| GitHub Repository | ✅ Completed |

---

# 🚀 Installation

Clone the repository

```bash
git clone https://github.com/ashuuuu7/Mutual_Fund_Analytics.git
```

Navigate to the project directory

```bash
cd Mutual_Fund_Analytics
```

Install all required dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Running the Project

Execute the project in the following sequence.

```text
01_data_ingestion.ipynb
          │
          ▼
02_data_cleaning.ipynb
          │
          ▼
03_eda_analysis.ipynb
          │
          ▼
04_performance_analytics.ipynb
          │
          ▼
05_advanced_analytics.ipynb
```

Run ETL Pipeline

```bash
python scripts/etl_pipeline.py
```

Open Dashboard

```text
dashboard/Mutual_Fund_Analytics_Dashboard.pbix
```

using Microsoft Power BI Desktop.

---

# 📈 Project Outcomes

This project successfully demonstrates an end-to-end Data Analytics workflow applied to real-world Mutual Fund data.

### Major Outcomes

- Automated ETL Pipeline developed
- SQLite relational database designed
- Advanced SQL analytics performed
- Comprehensive Exploratory Data Analysis completed
- Financial Performance Metrics calculated
- Advanced Risk Analytics implemented
- Interactive Power BI Dashboard developed
- Professional Report & Presentation prepared
- GitHub Portfolio Documentation completed

---

# 🔮 Future Scope

Potential future enhancements include:

- 🌐 Streamlit Web Application
- ⏰ Automated NAV Scheduler (Cron Jobs)
- 📈 Monte Carlo Simulation
- 📊 Markowitz Efficient Frontier
- 📧 Automated Email Reporting
- ☁️ Cloud Deployment
- 🤖 Machine Learning-based Fund Recommendation
- 🔗 REST API Integration
- 📱 Mobile Dashboard Support

---

# 🏅 Skills Demonstrated

### Programming

- Python
- SQL

### Data Engineering

- ETL Pipeline
- Data Cleaning
- Data Validation

### Database

- SQLite
- SQL Query Optimization

### Analytics

- Exploratory Data Analysis
- Financial Performance Analytics
- Risk Analytics
- Business Intelligence

### Visualization

- Power BI
- Matplotlib

### Tools

- Git
- GitHub
- Jupyter Notebook
- VS Code

---

# 👨‍💻 Author

## Ashutosh Giri

**B.Tech – Artificial Intelligence & Data Science**

University School of Automation & Robotics

Guru Gobind Singh Indraprastha University (GGSIPU)

### 📬 Connect with Me

- **GitHub:** https://github.com/ashuuuu7
- **LinkedIn:** https://www.linkedin.com/in/ashutosh-giri-datascience

---

# 🙏 Acknowledgement

I sincerely thank **Bluestock Fintech** for providing the opportunity to work on this capstone project.

This project significantly enhanced my practical understanding of:

- Financial Data Analytics
- Python Programming
- SQL & SQLite
- Power BI Dashboard Development
- Business Intelligence
- Risk Analytics
- End-to-End Data Analytics Workflow

I am grateful for the valuable learning experience and guidance throughout this internship.

---

# 📜 License

This repository is intended for **educational, internship, and portfolio purposes**.

© 2026 Ashutosh Giri. All Rights Reserved.

---

<div align="center">

## ⭐ If you found this project useful, consider giving it a Star!

### Thank you for visiting this repository.

</div>