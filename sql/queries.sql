SELECT
scheme_name,
aum_crore
FROM fact_performance
ORDER BY aum_crore DESC
LIMIT 5;


SELECT
amfi_code,
AVG(nav) AS avg_nav
FROM fact_nav
GROUP BY amfi_code;


SELECT
state,
COUNT(*) AS total_transactions
FROM fact_transactions
GROUP BY state
ORDER BY total_transactions DESC;


SELECT
scheme_name,
expense_ratio_pct
FROM fact_performance
WHERE expense_ratio_pct < 1;


SELECT
SUM(amount_inr) AS total_sip_amount
FROM fact_transactions
WHERE transaction_type='SIP';


SELECT
category,
AVG(return_3yr_pct) AS avg_return
FROM fact_performance
GROUP BY category;


SELECT
transaction_type,
COUNT(*) AS total_count
FROM fact_transactions
GROUP BY transaction_type;

SELECT
city,
COUNT(*) AS total_transactions
FROM fact_transactions
GROUP BY city
ORDER BY total_transactions DESC
LIMIT 10;


SELECT
gender,
AVG(amount_inr) AS avg_amount
FROM fact_transactions
GROUP BY gender;


SELECT
risk_grade,
COUNT(*) AS total_funds
FROM fact_performance
GROUP BY risk_grade;