
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

conn = sqlite3.connect("sales_data.db")
query = "SELECT product, SUM(quantity) AS total_qty, SUM(quantity * price) AS revenue FROM sales GROUP BY product"
df = pd.read_sql_query(query, conn)
conn.close()

print(df)

plt.bar(df["product"], df["revenue"])
plt.title("Revenue by Product")
plt.savefig("sales_chart.png")
