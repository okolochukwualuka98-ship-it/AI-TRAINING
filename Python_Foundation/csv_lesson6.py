import pandas as pd

employees = pd.read_csv("employees.csv")

lowest_employee = employees.loc[employees["Score"].idxmin()]

print(lowest_employee)