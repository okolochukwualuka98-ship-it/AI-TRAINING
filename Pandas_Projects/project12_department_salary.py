import sqlite3
import pandas as pd

conn = sqlite3.connect("company.db")

query = """
SELECT
    Department,
    ROUND(AVG(Salary), 2) AS Average_Salary
FROM employees
GROUP BY Department
ORDER BY Average_Salary DESC
"""

result = pd.read_sql(query, conn)

print(result)