import pandas as pd

df = pd.read_excel("Clean_Company_Data.xlsx")

print("EMPLOYEES BY DEPARTMENT")
print(df.groupby("Department")["Employee_ID"].count())

print("\nAVERAGE SALARY BY DEPARTMENT")
print(df.groupby("Department")["Salary"].mean())

print("\nAVERAGE PERFORMANCE BY DEPARTMENT")
print(df.groupby("Department")["Performance_Score"].mean())

print("\nEMPLOYEES BY REGION")
print(df.groupby("Region")["Employee_ID"].count())