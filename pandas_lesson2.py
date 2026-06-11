import pandas as pd

data = {
    "Name": ["John", "Mary", "Peter", "Grace"],
    "Age": [20, 22, 21, 23]
}

students = pd.DataFrame(data)

print(students)