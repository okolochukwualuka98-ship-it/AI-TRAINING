import pandas as pd

employees = pd.read_csv("employees.csv")

top_3 = employees.sort_values("Salary", ascending=False).head(3)

print(top_3)