import pandas as pd
import os

files = ["02_nav_history.csv", "07_scheme_performance.csv", "08_investor_transactions.csv"]

for file in files:
    data = pd.read_csv(f"data/raw/{file}")

    print("\n" + "="*60)
    print(file)
    print("="*60)
    print("Columns:")
    print(data.columns.tolist())
    print("\nShape:", data.shape)
    print("\nFirst 5 Rows:")
    print(data.head())
    print("\nMissing Values:")
    print(data.isnull().sum())
    print("\nDuplicate Rows:")
    print(data.duplicated().sum())
    print("\nUnique Values:")

    for col in data.columns:
        if data[col].nunique() < 15:
            print(f"\n{col}")
            print(data[col].unique())

os.makedirs("data/processed", exist_ok=True)

nav = pd.read_csv("data/raw/02_nav_history.csv")
nav["date"] = pd.to_datetime(nav["date"])
nav = nav.sort_values(["amfi_code", "date"])
nav = nav.drop_duplicates()
nav = nav[nav["nav"] > 0]
nav.to_csv("data/processed/02_nav_history_cleaned.csv", index=False)
print("NAV History Saved")
performance = pd.read_csv("data/raw/07_scheme_performance.csv")
performance = performance.drop_duplicates()
performance.to_csv("data/processed/07_scheme_performance_cleaned.csv", index=False)
print("Scheme Performance Saved")
transactions = pd.read_csv("data/raw/08_investor_transactions.csv")
transactions["transaction_date"] = pd.to_datetime(transactions["transaction_date"])
transactions = transactions[transactions["amount_inr"] > 0]
transactions = transactions.drop_duplicates()
transactions.to_csv("data/processed/08_investor_transactions_cleaned.csv", index=False)
print("Investor Transactions Saved")