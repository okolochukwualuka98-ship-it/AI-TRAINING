import sqlite3
import pandas as pd

conn = sqlite3.connect("company.db")

query = """
SELECT
    Product,
    SUM(Sales_Amount) AS Total_Sales
FROM employees
GROUP BY Product
ORDER BY Total_Sales DESC
LIMIT 10
"""

result = pd.read_sql(query, conn)

print(result)