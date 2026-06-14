import pandas as pd

employees = pd.read_csv("employees.csv")

bottom_2 = employees.sort_values("Score").head(2)

print(bottom_2)