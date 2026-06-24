# Data Dictionary

## fact_nav

| Column    | Data Type | Description             |
| --------- | --------- | ----------------------- |
| amfi_code | INTEGER   | Unique AMFI scheme code |
| date      | DATE      | NAV date                |
| nav       | REAL      | Net Asset Value         |

---

## fact_performance

| Column            | Data Type | Description                       |
| ----------------- | --------- | --------------------------------- |
| amfi_code         | INTEGER   | Unique AMFI scheme code           |
| scheme_name       | TEXT      | Mutual fund scheme name           |
| fund_house        | TEXT      | Asset management company          |
| category          | TEXT      | Fund category                     |
| plan              | TEXT      | Direct or Regular plan            |
| return_1yr_pct    | REAL      | 1-year return percentage          |
| return_3yr_pct    | REAL      | 3-year return percentage          |
| return_5yr_pct    | REAL      | 5-year return percentage          |
| aum_crore         | REAL      | Assets under management in crores |
| expense_ratio_pct | REAL      | Expense ratio percentage          |
| risk_grade        | TEXT      | Risk classification               |

---

## fact_transactions

| Column             | Data Type | Description                    |
| ------------------ | --------- | ------------------------------ |
| investor_id        | TEXT      | Investor identifier            |
| transaction_date   | DATE      | Transaction date               |
| amfi_code          | INTEGER   | Scheme code                    |
| transaction_type   | TEXT      | SIP, Lumpsum or Redemption     |
| amount_inr         | REAL      | Transaction amount in INR      |
| state              | TEXT      | Investor state                 |
| city               | TEXT      | Investor city                  |
| city_tier          | TEXT      | T30 or B30 city classification |
| age_group          | TEXT      | Investor age bracket           |
| gender             | TEXT      | Investor gender                |
| annual_income_lakh | REAL      | Annual income in lakhs         |
| payment_mode       | TEXT      | Payment method                 |
| kyc_status         | TEXT      | KYC verification status        |
