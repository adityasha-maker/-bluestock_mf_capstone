# Data Dictionary

## dim_fund
- amfi_code: Unique AMFI scheme code
- fund_house: Mutual fund company name
- scheme_name: Scheme name
- category: Fund category
- plan: Direct/Regular plan
- risk_category: Risk classification

## fact_nav
- amfi_code: Scheme code
- date: NAV date
- nav: Net Asset Value

## fact_transactions
- investor_id: Investor identifier
- transaction_date: Transaction date
- transaction_type: SIP/Lumpsum/Redemption
- amount_inr: Transaction amount
- state: Investor state
- city: Investor city
- kyc_status: KYC verification status

## fact_performance
- return_1yr_pct: 1-year return
- return_3yr_pct: 3-year return
- return_5yr_pct: 5-year return
- alpha: Alpha measure
- beta: Beta measure
- sharpe_ratio: Sharpe ratio
- aum_crore: Assets under management
- expense_ratio_pct: Expense ratio

## Data Quality Checks
- Removed duplicates
- Standardized dates
- Forward-filled missing NAV values
- Validated positive NAV values
- Validated transaction amounts
- Checked KYC status values
- Checked expense ratio anomalies