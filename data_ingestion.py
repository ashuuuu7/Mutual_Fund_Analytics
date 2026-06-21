import pandas as pd 
import os 

data = "data/raw"

files = os.listdir(data)

for file in files:
    if file.endswith(".csv"):
        print("\n" + "="*50)
        print("FILE:", file)
    
        df = pd.read_csv(os.path.join(data, file))

        print("Shape")
        print(df.shape)


        print("\nData Types:")
        print(df.dtypes)

        print("\nFirst 5 Rows:")
        print(df.head())

        print("\nMissing Values" )
        print(df.isnull().sum())

        if file == "01_fund_master.csv":
            print(df.columns)
            print(df.head())

            print("\nUnique Fund Houses:")

            print(df['fund_house'].nunique())

            print("\nFund Houses:")
            print(df['fund_house'].unique())

            print("\nCategories:")
            print(df['category'].unique())

            print("\nSub Categories:")
            print(df['sub_category'].unique())

            print("\nRisk Categories:")
            print(df['risk_category'].unique())

    fund_master = pd.read_csv("data/raw/01_fund_master.csv")
    nav_history = pd.read_csv("data/raw/02_nav_history.csv")

    missing_codes = set(fund_master["amfi_code"]) - set(nav_history["amfi_code"])

    print("Missing Codes:", len(missing_codes))
    
    print(missing_codes)