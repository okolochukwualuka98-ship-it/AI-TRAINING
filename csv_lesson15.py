import pandas as pd

employees = pd.read_csv("employees.csv")

print("Average Salary:", employees["Salary"].mean())
print("Highest Salary:", employees["Salary"].max())
print("Lowest Salary:", employees["Salary"].min())
print("Average Score:", employees["Score"].mean())