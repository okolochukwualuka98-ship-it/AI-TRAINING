import pandas as pd

employees = pd.read_csv("employees.csv")

department_summary = employees.groupby("Department")["Salary"].mean()

print("Average Salary by Department:")
print(department_summary)