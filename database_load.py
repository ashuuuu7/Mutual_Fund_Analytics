import sqlalchemy
import pandas as pd

from sqlalchemy import create_engine

engine = create_engine("sqlite:///bluestock_mf.db")
nav = pd.read_csv("data/processed/02_nav_history_cleaned.csv")
performance = pd.read_csv("data/processed/07_scheme_performance_cleaned.csv")
transactions = pd.read_csv("data/processed/08_investor_transactions_cleaned.csv")
nav.to_sql("fact_nav", engine, if_exists="replace", index=False)
performance.to_sql("fact_performance", engine, if_exists="replace", index=False)
transactions.to_sql("fact_transactions", engine, if_exists="replace", index=False)
print("Database Loaded Successfully")

import sqlite3

conn = sqlite3.connect("bluestock_mf.db")
cursor = conn.cursor()

cursor.execute(
    "SELECT name FROM sqlite_master WHERE type='table';"
)

print(cursor.fetchall())

conn.close()