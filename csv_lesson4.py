import pandas as pd

employees = pd.read_csv("employees.csv")

it_employees = employees[employees["Department"] == "IT"]

print("Average IT Salary:")
print(it_employees["Salary"].mean())