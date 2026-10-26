import pandas as pd
import sqlite3

df = pd.read_csv("data/cleaned_retail.csv")

with sqlite3.connect("data/retail_sales.db") as connection:
    df.to_sql("sales", connection, if_exists="replace", index=False)

print("Loaded", len(df), "rows into data/retail_sales.db")