import pandas as pd

data = {
    "Employee": ["John", "Mary", "Peter", "Grace", "David"],
    "Department": ["IT", "HR", "IT", "Finance", "IT"],
    "Salary": [250000, 180000, 300000, 220000, 280000]
}

employees = pd.DataFrame(data)

promotion_candidates = employees[employees["Salary"] >= 280000]

print("PROMOTION CANDIDATES")
print(promotion_candidates)