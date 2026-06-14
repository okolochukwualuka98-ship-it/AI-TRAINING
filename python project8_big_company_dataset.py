import pandas as pd
import numpy as np

np.random.seed(42)

employees = 800000

products = [f"Product_{i}" for i in range(1, 101)]

departments = [
    "Sales",
    "Marketing",
    "Finance",
    "HR",
    "IT",
    "Operations"
]

regions = [
    "North",
    "South",
    "East",
    "West"
]

data = {
    "Employee_ID": range(1, employees + 1),
    "Department": np.random.choice(departments, employees),
    "Region": np.random.choice(regions, employees),
    "Product": np.random.choice(products, employees),
    "Salary": np.random.randint(100000, 1000000, employees),
    "Performance_Score": np.random.randint(1, 11, employees),
    "Experience_Years": np.random.randint(1, 31, employees),
    "Sales_Amount": np.random.randint(50000, 5000000, employees)
}

df = pd.DataFrame(data)

df.to_excel("Big_Company_Data.xlsx", index=False)

print(df.head())
print("\nTotal Records:", len(df))