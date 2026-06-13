import pandas as pd
import numpy as np

employees = pd.read_csv("employees_1000.csv")

# Create some realistic data issues
employees.loc[5, "Salary"] = np.nan
employees.loc[15, "Salary"] = np.nan
employees.loc[25, "Score"] = np.nan

# Add duplicate rows
employees = pd.concat([employees, employees.iloc[[0, 1]]])

print("DATASET SHAPE:")
print(employees.shape)

print("\nMISSING VALUES:")
print(employees.isnull().sum())

print("\nDUPLICATE ROWS:")
print(employees.duplicated().sum())