import pandas as pd

employees = pd.read_csv("employees_1000.csv")

promotion_candidates = employees[
    employees["Score"] >= 90
]

print("PROMOTION CANDIDATES")
print(promotion_candidates)

print()
print("TOTAL CANDIDATES:", len(promotion_candidates))