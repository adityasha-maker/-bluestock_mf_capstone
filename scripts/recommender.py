import pandas as pd

base_path = r"C:\Users\sharm\OneDrive\Desktop\DATASETS CSV"

perf = pd.read_csv(f"{base_path}\\07_scheme_performance.csv")

recommendation = (
    perf[['scheme_name', 'risk_grade', 'sharpe_ratio']]
    .sort_values('sharpe_ratio', ascending=False)
)

def recommend_funds(risk_level):
    funds = recommendation[
        recommendation['risk_grade']
        .str.contains(risk_level, case=False, na=False)
    ]
    return funds.head(3)

print("LOW RISK")
print(recommend_funds("Low"))

print("\nMODERATE RISK")
print(recommend_funds("Moderate"))

print("\nHIGH RISK")
print(recommend_funds("High"))