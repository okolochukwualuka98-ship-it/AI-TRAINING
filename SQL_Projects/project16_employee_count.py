import sqlite3
import pandas as pd

conn = sqlite3.connect("company.db")

query = """
SELECT
    Department,
    COUNT(*) AS Employee_Count
FROM employees
GROUP BY Department
ORDER BY Employee_Count DESC
"""

result = pd.read_sql(query, conn)

print(result)