-- 1 Top 5 Funds by AUM
SELECT scheme_name, aum_crore
FROM fact_performance
ORDER BY aum_crore DESC
LIMIT 5;

-- 2 Average NAV per Fund
SELECT amfi_code,
AVG(nav) AS avg_nav
FROM fact_nav
GROUP BY amfi_code;

-- 3 Transactions by State
SELECT state,
COUNT(*) AS total_transactions
FROM fact_transactions
GROUP BY state
ORDER BY total_transactions DESC;

-- 4 SIP Transactions
SELECT COUNT(*) AS sip_count
FROM fact_transactions
WHERE transaction_type='SIP';

-- 5 Funds with Expense Ratio < 1%
SELECT scheme_name,
expense_ratio_pct
FROM fact_performance
WHERE expense_ratio_pct < 1;

-- 6 Highest Sharpe Ratio
SELECT scheme_name,
sharpe_ratio
FROM fact_performance
ORDER BY sharpe_ratio DESC;

-- 7 Highest Alpha
SELECT scheme_name,
alpha
FROM fact_performance
ORDER BY alpha DESC;

-- 8 Average Return by Category
SELECT category,
AVG(return_3yr_pct)
FROM fact_performance
GROUP BY category;

-- 9 Risk Grade Distribution
SELECT risk_grade,
COUNT(*)
FROM fact_performance
GROUP BY risk_grade;

-- 10 Total Transaction Amount
SELECT SUM(amount_inr)
FROM fact_transactions;