import pandas as pd

print("Loading Dataset...")

df = pd.read_excel("Big_Company_Data.xlsx")

print("\nDATA INSPECTION")
print("=" * 40)

print("\nFIRST 5 ROWS")
print(df.head())

print("\nLAST 5 ROWS")
print(df.tail())

print("\nDATA SHAPE")
print(df.shape)

print("\nCOLUMN NAMES")
print(df.columns)

print("\nDATA TYPES")
print(df.dtypes)
print("\nMISSING VALUES")
print("=" * 40)

print(df.isnull().sum())
print("\nDUPLICATE RECORDS")
print("=" * 40)

print(df.duplicated().sum())
print("\nDATA VALIDATION")
print("=" * 40)

print("Negative Salary:",
      (df["Salary"] < 0).sum())

print("Negative Sales:",
      (df["Sales_Amount"] < 0).sum())

print("Negative Experience:",
      (df["Experience_Years"] < 0).sum())

print("Performance > 10:",
      (df["Performance_Score"] > 10).sum())
df.to_excel(
    "Clean_Company_Data.xlsx",
    index=False
)

print("\nClean Dataset Exported Successfully!")

