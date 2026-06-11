# Bluestock Mutual Fund Analytics Capstone

## Project Overview

This project was developed as part of the Bluestock Fintech Data Analyst Internship Program. The objective is to perform end-to-end mutual fund analytics using real-world financial datasets covering fund performance, investor transactions, SIP trends, portfolio holdings, and industry-level metrics.

The project implements a complete analytics pipeline including data ingestion, data cleaning, exploratory data analysis, performance analytics, advanced risk analytics, and interactive dashboard development.

---

## Objectives

* Build an ETL pipeline for mutual fund datasets
* Clean and validate financial data
* Perform exploratory data analysis (EDA)
* Compute fund performance metrics
* Analyze investor behavior and SIP trends
* Calculate risk metrics such as VaR and CVaR
* Build a simple mutual fund recommendation engine
* Develop an interactive Power BI dashboard

---

## Project Architecture

Raw Data → ETL Pipeline → Data Cleaning → SQLite Database → EDA → Performance Analytics → Advanced Analytics → Power BI Dashboard → Final Reporting

---

## Datasets Used

1. Fund Master
2. NAV History
3. AUM by Fund House
4. Monthly SIP Inflows
5. Category Inflows
6. Industry Folio Count
7. Scheme Performance
8. Investor Transactions
9. Portfolio Holdings
10. Benchmark Indices

---

## Folder Structure

```text
bluestock_mf_capstone/
├── data/
├── notebooks/
├── scripts/
├── sql/
├── dashboard/
├── reports/
└── README.md
```

## Technologies Used

* Python
* Pandas
* NumPy
* SQLAlchemy
* SQLite
* Matplotlib
* Seaborn
* Plotly
* Power BI
* Jupyter Notebook
* Git & GitHub

---

## Key Analyses

### Exploratory Data Analysis

* NAV trend analysis
* AUM growth analysis
* SIP inflow trends
* Investor demographics
* Geographic investment distribution
* Category-wise fund inflows

### Performance Analytics

* CAGR
* Sharpe Ratio
* Sortino Ratio
* Alpha & Beta
* Maximum Drawdown
* Fund Scorecard

### Advanced Analytics

* Value at Risk (VaR)
* Conditional Value at Risk (CVaR)
* Rolling Sharpe Ratio
* Investor Cohort Analysis
* SIP Continuity Analysis
* Sector Concentration Risk (HHI)
* Fund Recommendation Engine

---

## Dashboard Pages

### Industry Overview

* Total AUM
* SIP Inflows
* Folios
* AUM Growth Trends

### Fund Performance

* Risk vs Return Analysis
* Fund Scorecard
* NAV Trend Analysis

### Investor Analytics

* Investor Demographics
* State-wise Investments
* Transaction Trends

### SIP & Market Trends

* SIP Growth Trends
* Category Inflows
* Market Correlation Analysis

---

## How to Run

Install dependencies:

```bash
pip install -r requirements.txt
```

Run notebooks in sequence:

1. 01_data_ingestion.ipynb
2. 02_data_cleaning.ipynb
3. 03_eda_analysis.ipynb
4. 04_performance_analytics.ipynb
5. 05_advanced_analytics.ipynb

Open the Power BI dashboard:

```text
dashboard/bluestock_mf_dashboard.pbix
```

---

## Future Improvements

* Real-time NAV updates
* Machine Learning based recommendation engine
* Portfolio optimization module
* Automated report generation
* Cloud deployment

---

## Author

Puru Asthana

Bluestock Fintech Data Analyst Internship Program
