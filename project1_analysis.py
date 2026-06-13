import pandas as pd

df = pd.read_csv("employees_1000.csv")

print("TOTAL EMPLOYEES:", len(df))

print("AVERAGE SALARY:", round(df["Salary"].mean(), 2))

print("HIGHEST SALARY:", df["Salary"].max())

print("LOWEST SALARY:", df["Salary"].min())

print("AVERAGE SCORE:", round(df["Score"].mean(), 2))

print("\nTOP PERFORMER:")
print(df.loc[df["Score"].idxmax()])