import pandas as pd

employees = pd.read_csv("employees.csv")

print("Average Salary:")
print(employees["Salary"].mean())