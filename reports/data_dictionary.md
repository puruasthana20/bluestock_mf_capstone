# Data Dictionary

## dim_fund

| Column | Type | Description |
|----------|----------|----------|
| amfi_code | INTEGER | Unique AMFI scheme identifier |
| fund_house | TEXT | Mutual fund company |
| scheme_name | TEXT | Mutual fund scheme name |
| category | TEXT | Fund category |
| sub_category | TEXT | Fund sub-category |
| plan | TEXT | Direct/Regular plan |

---

## fact_nav

| Column | Type | Description |
|----------|----------|----------|
| amfi_code | INTEGER | Scheme identifier |
| date | DATE | NAV date |
| nav | REAL | Net Asset Value |

---

## fact_transactions

| Column | Type | Description |
|----------|----------|----------|
| investor_id | TEXT | Investor identifier |
| transaction_date | DATE | Transaction date |
| transaction_type | TEXT | SIP/Lumpsum/Redemption |
| amount_inr | REAL | Transaction amount |

---

## fact_performance

| Column | Type | Description |
|----------|----------|----------|
| return_1yr_pct | REAL | 1 Year Return |
| return_3yr_pct | REAL | 3 Year Return |
| sharpe_ratio | REAL | Risk-adjusted return |
| beta | REAL | Volatility measure |

---

## fact_aum

| Column | Type | Description |
|----------|----------|----------|
| fund_house | TEXT | Mutual fund company |
| aum_crore | REAL | Assets Under Management |