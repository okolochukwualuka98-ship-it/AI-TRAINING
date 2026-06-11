import pandas as pd

employees = pd.read_csv("employees.csv")

top_2 = employees.sort_values("Score", ascending=False).head(2)

print(top_2)