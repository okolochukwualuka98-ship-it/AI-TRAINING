import sqlite3
import pandas as pd

conn = sqlite3.connect("company.db")

query = """
SELECT
    Region,
    SUM(Sales_Amount) AS Total_Sales
FROM employees
GROUP BY Region
ORDER BY Total_Sales DESC
"""

result = pd.read_sql(query, conn)

print(result)