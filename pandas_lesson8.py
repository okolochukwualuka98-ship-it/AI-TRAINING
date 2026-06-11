import pandas as pd

data = {
    "Name": ["John", "Mary", "Peter", "Grace"],
    "Age": [20, 22, 21, 23]
}

students = pd.DataFrame(data)

print("Average Age:", students["Age"].mean())
print("Highest Age:", students["Age"].max())
print("Lowest Age:", students["Age"].min())
print("Total Age:", students["Age"].sum())