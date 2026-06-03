-- 1. Top 5 Funds by AUM

SELECT scheme_name,
       aum_crore
FROM fact_performance
ORDER BY aum_crore DESC
LIMIT 5;


-- 2. Average NAV by Month

SELECT strftime('%Y-%m', date) AS month,
       AVG(nav) AS avg_nav
FROM fact_nav
GROUP BY month
ORDER BY month;


-- 3. Transactions by State

SELECT state,
       COUNT(*) AS transaction_count
FROM fact_transactions
GROUP BY state
ORDER BY transaction_count DESC;


-- 4. Funds with Expense Ratio < 1%

SELECT scheme_name,
       expense_ratio_pct
FROM fact_performance fp
JOIN dim_fund df
ON fp.amfi_code = df.amfi_code
WHERE expense_ratio_pct < 1;


-- 5. Average Return by Category

SELECT category,
       AVG(return_3yr_pct) AS avg_return
FROM fact_performance fp
JOIN dim_fund df
ON fp.amfi_code = df.amfi_code
GROUP BY category;


-- 6. Top 10 Funds by Sharpe Ratio

SELECT scheme_name,
       sharpe_ratio
FROM fact_performance fp
JOIN dim_fund df
ON fp.amfi_code = df.amfi_code
ORDER BY sharpe_ratio DESC
LIMIT 10;


-- 7. Investor Count by Gender

SELECT gender,
       COUNT(*) AS investor_count
FROM fact_transactions
GROUP BY gender;


-- 8. Investor Count by Age Group

SELECT age_group,
       COUNT(*) AS investor_count
FROM fact_transactions
GROUP BY age_group
ORDER BY investor_count DESC;


-- 9. Average Transaction Amount by Type

SELECT transaction_type,
       AVG(amount_inr) AS avg_amount
FROM fact_transactions
GROUP BY transaction_type;


-- 10. Fund Houses by Total AUM

SELECT fund_house,
       SUM(aum_crore) AS total_aum
FROM fact_aum
GROUP BY fund_house
ORDER BY total_aum DESC;
