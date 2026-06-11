import pandas as pd

data = {
    "Name": ["John", "Mary", "Peter", "Grace"],
    "Score": [85, 92, 78, 95]
}

students = pd.DataFrame(data)

print(students)
print("Average Score:", students["Score"].mean())
print("Highest Score:", students["Score"].max())
print("Lowest Score:", students["Score"].min())