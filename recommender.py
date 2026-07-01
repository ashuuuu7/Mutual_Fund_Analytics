import pandas as pd

# Load performance dataset
performance = pd.read_csv("data/processed/07_scheme_performance_cleaned.csv")

print("=" * 50)
print("Mutual Fund Recommendation System")
print("=" * 50)

risk = input("\nEnter Risk Appetite (Low / Moderate / High): ").strip().title()

# Filter funds based on risk grade
filtered = performance[
    performance["risk_grade"].str.title() == risk
]

if filtered.empty:
    print("\nNo funds found for the selected risk level.")
else:
    recommendations = (
        filtered.sort_values(
            by="sharpe_ratio",
            ascending=False
        )
        .head(3)
    )

    print(f"\nTop 3 Recommended Funds for {risk} Risk\n")

    print(
        recommendations[
            [
                "scheme_name",
                "risk_grade",
                "sharpe_ratio"
            ]
        ].to_string(index=False)
    )