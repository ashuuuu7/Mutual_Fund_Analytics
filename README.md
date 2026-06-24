# Mutual Fund Analytics

## Bluestock Fintech Capstone Project

A comprehensive Data Analytics project focused on Mutual Fund data processing, cleaning, database design, and analytical reporting using Python, SQL, and SQLite.

---

## Project Overview

This project analyzes mutual fund datasets to generate insights related to fund performance, NAV trends, investor transactions, AUM distribution, and portfolio analytics.

The project follows a complete data analytics workflow:

* Data Ingestion (ETL)
* Data Cleaning & Validation
* Database Design
* SQL Analytics
* Data Documentation
* Dashboard Development (Upcoming)

---

## Day 1: Project Setup & Data Ingestion

### Tasks Completed

* Created project folder structure
* Initialized Git repository and connected GitHub
* Installed required Python libraries
* Loaded and explored 10 mutual fund datasets using Pandas
* Checked dataset dimensions, data types, and sample records
* Performed missing value analysis
* Explored fund master dataset
* Validated AMFI scheme codes
* Fetched live NAV data from MFAPI
* Retrieved NAV history for 5 major mutual fund schemes
* Generated data quality summary

### Deliverables

* data_ingestion.py
* live_nav_fetch.py
* requirements.txt
* GitHub repository with Day 1 commit

---

## Day 2: Data Cleaning & Database Design

### Tasks Completed

#### Data Cleaning

* Parsed date columns into datetime format
* Removed duplicate records
* Validated NAV values (> 0)
* Validated transaction amounts (> 0)
* Standardized transaction records
* Performed categorical value validation
* Generated cleaned datasets

#### Database Development

* Created SQLite database (bluestock_mf.db)
* Loaded cleaned datasets into SQLite using SQLAlchemy
* Created database schema design
* Implemented fact tables for:

  * NAV History
  * Fund Performance
  * Investor Transactions

#### SQL Analytics

Created analytical SQL queries for:

* Top 5 Funds by AUM
* Average NAV by Fund
* Transactions by State
* Expense Ratio Analysis
* SIP Investment Analysis
* Category Performance Analysis
* Transaction Distribution Analysis
* City-wise Transaction Analysis
* Gender-wise Investment Analysis
* Risk Grade Distribution

#### Documentation

* Created schema.sql
* Created queries.sql
* Created data_dictionary.md

### Deliverables

* data_cleaning.py
* database_load.py
* schema.sql
* queries.sql
* data_dictionary.md
* bluestock_mf.db

---

## Project Structure

```text
Mutual_Fund_Analytics/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── notebooks/
├── sql/
├── dashboard/
├── reports/
│
├── data_ingestion.py
├── live_nav_fetch.py
├── data_cleaning.py
├── database_load.py
├── requirements.txt
├── README.md
└── bluestock_mf.db
```

## Technologies Used

* Python
* Pandas
* NumPy
* SQLAlchemy
* SQLite
* Requests
* Git
* GitHub

---

## Current Progress

### Completed

* Data Ingestion
* Data Validation
* Data Cleaning
* SQLite Database Design
* Data Loading
* SQL Analytics
* Documentation

### Upcoming

* Dashboard Development
* Advanced Analytics
* Reporting & Visualization
* Final Capstone Submission

---

## Author

**Ashutosh Giri**

B.Tech Artificial Intelligence & Data Science
GGSIPU – University School of Automation and Robotics

Bluestock Fintech Data Analyst Internship – 2026
