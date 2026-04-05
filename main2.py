import pandas as pd 
import numpy as np

# grades = np.random.randint(0, 12, size=(25, 10))
# df = pd.DataFrame(grades, columns=["Math", "History", "English", "Literature", "Physics", "Ukrainian", "Biology", "PE", "Chemistry", "Geography"])
# print(df)

# data = {
#     'Name': ['Anna', 'Boris', 'Clara', 'Diana'],
#     'Age': [28, 34, 29, 42],
#     'City': ['Kyiv', 'Lviv', 'Odesa', 'Dnipro']
# }

# df = pd.DataFrame(data)
# print(df.loc[df["Age"] > 30], "Name")

# Створіть двовимірний NumPy масив розміру 4x2 з випадковими
# числами з нормальним розподілом (середнє=50, стандартне відхилення=5).
# Перетворіть цей масив на DataFrame з назвами стовпців ['Height', 'Weight'

# data = np.random.normal(loc=50, scale=5, size=(4, 2))
# df = pd.DataFrame(data, columns=['Height', 'Weight'])
# print(df)


# Створіть словник з наступними ключами та значеннями:
# 'Product': ['Laptop', 'Smartphone', 'Tablet']
# 'Price': [1200, 800, 400]
# 'Stock': [50, 150, 200]
# Перетворіть цей словник на DataFrame.

# data = {
#     'Product': ['Laptop', 'Smartphone', 'Tablet'],
#     'Price': [1200, 800, 400],
#     'Stock': [50, 150, 200]
# }
# df = pd.DataFrame(data)
# print(df)

# Створіть список списків, де кожний внутрішній список
# містить дані про студентів: ім'я, вік та оцінку.
# Перетворіть цей список на DataFrame з назвами стовпців ['Name', 'Age', 'Score'].
# data = [
#     ['John', 22, 88],
#     ['Alice', 23, 92],
#     ['Bob', 24, 75]
# ]

data = {
    'Product': ['Laptop', 'Smartphone', 'Tablet'],
    'Price': [1200, 800, 400],
    'Stock': [50, 150, 200]
}

df = pd.DataFrame(data)

df["Category"] = "Electronics"

df["New_Price"] = df["Price"] * 1.2

df['Level'] = np.where(df['Price'] < 800, 'low', 'high')

print(df)