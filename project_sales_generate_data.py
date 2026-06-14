import pandas as pd
import random

products = [
    "Laptop",
    "Phone",
    "Tablet",
    "Printer",
    "Monitor",
    "Keyboard",
    "Mouse",
    "Router"
]

regions = [
    "North",
    "South",
    "East",
    "West"
]

data = []

for i in range(1, 5001):

    product = random.choice(products)

    region = random.choice(regions)

    quantity = random.randint(1, 20)

    price = random.randint(50000, 800000)

    revenue = quantity * price

    data.append([
        i,
        product,
        region,
        quantity,
        price,
        revenue
    ])

sales = pd.DataFrame(
    data,
    columns=[
        "Sale_ID",
        "Product",
        "Region",
        "Quantity",
        "Price",
        "Revenue"
    ]
)

sales.to_excel(
    "Raw_Sales_Data.xlsx",
    index=False
)

print("Raw Sales Data Created Successfully!")
print(sales.head())             