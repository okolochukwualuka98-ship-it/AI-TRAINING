import pandas as pd

employees = pd.read_csv("employees.csv")

high_performers = employees[employees["Score"] >= 80]

high_performers.to_excel(
    "High_Performers_Report.xlsx",
    index=False
)

print("Report exported successfully!")