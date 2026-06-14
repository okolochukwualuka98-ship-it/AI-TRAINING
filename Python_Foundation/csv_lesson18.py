import pandas as pd

employees = pd.read_csv("employees.csv")

average_score = employees["Score"].mean()

above_average = employees[employees["Score"] > average_score]

print("Average Score:", average_score)
print("\nEmployees Above Average:")
print(above_average)