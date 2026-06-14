import pandas as pd
import random

departments = [
    "IT",
    "HR",
    "Finance",
    "Marketing",
    "Operations",
    "Sales",
    "Engineering",
    "Customer Support"
]

data = []

for i in range(1, 1001):
    employee = f"Employee_{i}"

    department = random.choice(departments)

    salary = random.randint(150000, 800000)

    score = random.randint(50, 100)

    experience = random.randint(1, 20)

    data.append([
        employee,
        department,
        salary,
        score,
        experience
    ])

employees = pd.DataFrame(
    data,
    columns=[
        "Employee",
        "Department",
        "Salary",
        "Score",
        "Experience"
    ]
)

employees.to_csv(
    "employees_1000.csv",
    index=False
)

print("Dataset created successfully!")
print(employees.head())