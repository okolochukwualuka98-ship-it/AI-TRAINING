import pandas as pd

employees = pd.read_csv("employees_1000.csv")

department_summary = employees.groupby("Department").agg({
    "Salary": "mean",
    "Score": "mean",
    "Employee": "count"
})

department_summary.columns = [
    "Average Salary",
    "Average Score",
    "Employee Count"
]

department_summary.to_excel(
    "Management_Report.xlsx"
)

print("Management Report Created Successfully!")