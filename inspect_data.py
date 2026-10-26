import pandas as pd

file_path = "data/Online Retail.xlsx"
df = pd.read_excel(file_path)

# Remove canceled invoices and invalid quantity or price rows
cleaned = df[
    ~df["InvoiceNo"].astype(str).str.startswith("C")
    & (df["Quantity"] > 0)
    & (df["UnitPrice"] > 0)
].copy()

cleaned["SalesValue"] = cleaned["Quantity"] * cleaned["UnitPrice"]
cleaned.to_csv("data/cleaned_retail.csv", index=False)

print("Original rows:", len(df))
print("Rows after cleaning:", len(cleaned))
print("Sales value (£):", round(cleaned["SalesValue"].sum(), 2))
print("Saved data/cleaned_retail.csv")