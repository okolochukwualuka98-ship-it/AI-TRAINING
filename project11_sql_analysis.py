import pandas as pd
import sqlite3

df = pd.read_excel("Clean_Company_Data.xlsx")

conn = sqlite3.connect("company.db")

df.to_sql(
    "employees",
    conn,
    if_exists="replace",
    index=False
)

print("Database Created Successfully!")