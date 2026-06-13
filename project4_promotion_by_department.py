import pandas as pd

employees = pd.read_csv("employees_1000.csv")

promotion_candidates = employees[
    employees["Score"] >= 90
]

department_promotions = promotion_candidates["Department"].value_counts()

print("PROMOTION CANDIDATES BY DEPARTMENT")
print(department_promotions)