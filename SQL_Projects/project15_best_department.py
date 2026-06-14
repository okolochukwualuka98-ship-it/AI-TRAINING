import sqlite3
import pandas as pd

conn = sqlite3.connect("company.db")

query = """
SELECT
    Department,
    ROUND(AVG(Performance_Score), 2) AS Avg_Performance
FROM employees
GROUP BY Department
ORDER BY Avg_Performance DESC
"""

result = pd.read_sql(query, conn)

print(result)