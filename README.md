# Mutual Fund Analytics Capstone

## Project Overview

This project analyzes Indian Mutual Fund data using Python, Pandas, SQL, SQLite, MFAPI, and Power BI.

## Objectives

* Build ETL Pipeline
* Clean and validate mutual fund datasets
* Create SQLite database
* Perform SQL analysis
* Fetch live NAV data using MFAPI
* Build Power BI Dashboard

## Tech Stack

* Python
* Pandas
* NumPy
* SQLite
* SQLAlchemy
* Requests
* Power BI
* Git & GitHub

## Project Structure

bluestock_mf_capstone/

├── reports/

├── scripts/

├── sql/

├── schema.sql

├── requirements.txt

├── README.md

## Day 1 Deliverables

* Project Setup
* Data Ingestion
* Dataset Profiling
* Data Dictionary
* Data Quality Report

## Day 2 Deliverables

* Data Cleaning
* SQLite Database Creation
* SQL Analysis Queries
* Live NAV Fetch using MFAPI

  ## Day 3 – Exploratory Data Analysis (EDA)

### Objectives

* Analyze Mutual Fund industry trends and fund performance patterns.
* Visualize NAV movements, SIP inflows, AUM growth, investor demographics, and portfolio allocations.
* Generate insights to support investment analysis.

### Tasks Completed

* NAV Trend Analysis for selected mutual fund schemes.
* SIP Inflow Trend Analysis.
* Fund-wise and category-wise comparisons.
* Correlation Analysis of fund returns.
* Investor demographic analysis.
* Geographic distribution analysis.
* Folio growth trend visualization.
* Sector allocation analysis.

### Deliverables

* `03_eda_analysis.ipynb`
* Multiple EDA charts and visualizations.
* Key analytical insights documented in notebook markdown cells.

### Key Findings

* Mutual fund participation increased significantly during the study period.
* SIP inflows showed a consistent upward trend.
* Equity-oriented schemes attracted higher investor interest.
* Fund return correlations highlighted diversification opportunities.
* Sector allocations indicated concentration in major industries such as Financial Services and IT.


## Day 4 – Fund Performance Analytics

### Objectives

* Evaluate historical mutual fund performance.
* Measure return generation and risk-adjusted returns.
* Compare schemes using industry-standard metrics.

### Tasks Completed

* Calculated Daily Returns using NAV data.
* Computed Compound Annual Growth Rate (CAGR).
* Calculated Sharpe Ratio for risk-adjusted performance evaluation.
* Ranked mutual fund schemes based on performance metrics.
* Generated performance visualizations.

### Performance Summary

| Scheme           | CAGR (%) | Sharpe Ratio |
| ---------------- | -------: | -----------: |
| HDFC Top 100     |    24.01 |         1.13 |
| Kotak Bluechip   |    16.82 |         0.72 |
| Nippon Large Cap |    15.12 |         0.59 |
| Axis Bluechip    |    51.18 |         0.27 |
| SBI Bluechip     |     0.15 |        -0.63 |
| ICICI Bluechip   |    15.49 |          NaN |

### Key Findings

* HDFC Top 100 delivered the strongest risk-adjusted returns.
* Kotak Bluechip and Nippon Large Cap demonstrated balanced risk-return characteristics.
* Axis Bluechip achieved the highest CAGR but exhibited lower risk-adjusted efficiency.
* SBI Bluechip underperformed relative to the assumed risk-free rate.
* ICICI Bluechip requires further data validation due to missing Sharpe Ratio values.

### Deliverables

* `04_performance_analytics.ipynb`
* `day4_performance_metrics.csv`
* `cagr_comparison.png`
* `sharpe_ratio_comparison.png


## Day 5 – Dashboard Development

### Objectives

Developed an interactive Power BI dashboard for mutual fund industry analysis, fund performance evaluation, investor behavior insights, and SIP market trend visualization.

### Dashboard Pages

#### 1. Industry Overview

* Total AUM KPI
* SIP Inflows KPI
* Total Folios KPI
* Number of Schemes KPI
* Industry AUM Trend
* AUM by Fund House

#### 2. Fund Performance

* Return vs Risk Scatter Plot
* Fund Scorecard Table
* NAV vs Benchmark Analysis
* Fund House and Category Slicers

#### 3. Investor Analytics

* Transaction Amount by State
* SIP/Lumpsum/Redemption Distribution
* Age Group Analysis
* City Tier Analysis
* Interactive Slicers

#### 4. SIP & Market Trends

* Monthly SIP Inflow Trend
* Nifty 50 Trend
* SIP Inflows vs Market Performance
* Category-wise Net Inflows
* Top 5 Categories by Net Inflow

### Deliverables

* bluestock_mf_dashboard.pbix
* Dashboard.pdf
* Dashboard Screenshots (PNG)

### Tools Used

* Power BI Desktop
* CSV Datasets
* Data Modeling
* Interactive Visualizations



## Author

Aditya Sharma
