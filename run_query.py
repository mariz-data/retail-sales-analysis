import csv
import sqlite3

with sqlite3.connect("data/retail_sales.db") as connection:
    rows = connection.execute("""
        SELECT
            substr(InvoiceDate, 1, 7) AS month,
            ROUND(SUM(SalesValue), 2) AS sales_value_gbp
        FROM sales
        GROUP BY month
        ORDER BY month
    """).fetchall()

with open("outputs/monthly_sales.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["month", "sales_value_gbp"])
    writer.writerows(rows)

print("Saved 13 monthly totals to outputs/monthly_sales.csv")