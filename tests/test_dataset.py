import pandas as pd

df = pd.read_csv("data/raw/online_retail.csv", nrows=5)

print(df.head())
# print(df.columns.tolist())
# print(df.dtypes)