import pandas as pd
import matplotlib.pyplot as plt

employees = pd.read_csv("employees.csv")

plt.bar(employees["Employee"], employees["Score"])

plt.title("Employee Scores")
plt.xlabel("Employee")
plt.ylabel("Score")

plt.show()