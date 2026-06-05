-- Top 5 Funds by AUM

SELECT
scheme_name,
aum_crore
FROM fact_performance
ORDER BY aum_crore DESC
LIMIT 5;

-- Average NAV

SELECT
AVG(nav)
FROM fact_nav;

-- Transaction Count

SELECT
transaction_type,
COUNT(*)
FROM fact_transactions
GROUP BY transaction_type;

-- State-wise Transactions

SELECT
state,
SUM(amount_inr)
FROM fact_transactions
GROUP BY state
ORDER BY SUM(amount_inr) DESC;

-- Expense Ratio Below 1%

SELECT
scheme_name,
expense_ratio_pct
FROM fact_performance
WHERE expense_ratio_pct < 1;

-- Top Sharpe Ratio

SELECT
scheme_name,
sharpe_ratio
FROM fact_performance
ORDER BY sharpe_ratio DESC;

-- Highest Alpha

SELECT
scheme_name,
alpha
FROM fact_performance
ORDER BY alpha DESC;

-- Average Return by Category

SELECT
category,
AVG(return_3yr_pct)
FROM fact_performance
GROUP BY category;

-- Risk Grade Distribution

SELECT
risk_grade,
COUNT(*)
FROM fact_performance
GROUP BY risk_grade;

-- Total Transaction Amount

SELECT
SUM(amount_inr)
FROM fact_transactions;