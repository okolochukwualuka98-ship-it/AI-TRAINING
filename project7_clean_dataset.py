import pandas as pd
import numpy as np

employees = pd.read_csv("employees_1000.csv")

# Create problems
employees.loc[5, "Salary"] = np.nan
employees.loc[15, "Salary"] = np.nan
employees.loc[25, "Score"] = np.nan

employees = pd.concat([employees, employees.iloc[[0, 1]]])

print("BEFORE CLEANING")
print(employees.shape)

# Fill missing values
employees["Salary"] = employees["Salary"].fillna(
    employees["Salary"].mean()
)

employees["Score"] = employees["Score"].fillna(
    employees["Score"].mean()
)

# Remove duplicates
employees = employees.drop_duplicates()

print()
print("AFTER CLEANING")
print(employees.shape)

print()
print("MISSING VALUES")
print(employees.isnull().sum())

print()
print("DUPLICATES")
print(employees.duplicated().sum())