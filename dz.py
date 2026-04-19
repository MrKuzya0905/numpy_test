import numpy as np
import pandas as pd 


# Завдання 1

data = {
    'Product': ['Laptop', 'Smartphone', 'Tablet'],
    'Price': [1200, 800, 400],
    'Stock': [50, 150, 200]
}
df = pd.DataFrame(data)

new_row = pd.DataFrame([{
    'Product': 'USB Hub',
    'Price': 40,
    'Stock': 150,
    'Warranty': '2 years'
}])

df = pd.concat([df, new_row], ignore_index=True)

print(df)
# Завдання 2

data = {
    'Product': ['Laptop', 'Smartphone', 'Tablet'],
    'Price': [1200, 800, 400],
    'Stock': [50, 150, 200]
}
df = pd.DataFrame(data)

new_row = pd.DataFrame([{
    'Product': 'USB Hub',
    'Price': 'Forty',  
    'Stock': 150
}])

df = pd.concat([df, new_row], ignore_index=True)

print(df)

#Завдання 3

df = pd.read_csv("customer_feedback.csv")

grouped = df.groupby(['Region', 'Month'])['Rating'].mean()

table = grouped.unstack()

table_filled = table.fillna(table.mean().mean())

print(table_filled)
