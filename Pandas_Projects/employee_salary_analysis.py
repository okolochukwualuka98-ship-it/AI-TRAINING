import pandas as pd

data = {
    "Employee": ["John", "Mary", "Peter", "Grace", "David"],
    "Department": ["IT", "HR", "IT", "Finance", "IT"],
    "Salary": [250000, 180000, 300000, 220000, 280000]
}

employees = pd.DataFrame(data)

print(employees)
print("Highest Salary:", employees["Salary"].max())
print("Lowest Salary:", employees["Salary"].min())
print("Average Salary:", employees["Salary"].mean())
print(employees[employees["Salary"] > 250000])
print(employees[employees["Department"] == "IT"])
