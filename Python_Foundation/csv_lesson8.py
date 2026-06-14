import pandas as pd

employees = pd.read_csv("employees.csv")

sorted_salary = employees.sort_values("Salary", ascending=False)

print(sorted_salary)