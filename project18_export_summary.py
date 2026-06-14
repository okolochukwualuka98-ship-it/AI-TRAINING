import pandas as pd

df = pd.read_excel("Clean_Company_Data.xlsx")

summary = df.groupby("Department").agg(
    Employee_Count=("Employee_ID", "count"),
    Average_Salary=("Salary", "mean"),
    Average_Performance=("Performance_Score", "mean"),
    Average_Experience=("Experience_Years", "mean")
)

summary.to_excel("Department_Summary_Report.xlsx")

print("Report exported successfully")