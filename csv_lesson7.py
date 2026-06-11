import pandas as pd

employees = pd.read_csv("employees.csv")

high_performers = employees[employees["Score"] >= 80]

print(high_performers)