import pandas as pd

employees = pd.read_csv("employees.csv")

top_employee = employees.loc[employees["Score"].idxmax()]

print("Top Performer:")
print(top_employee)