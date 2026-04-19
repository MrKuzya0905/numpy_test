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
# print(df.loc[df["Age"] > 20], "Name")

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

# data = {
#     'Product': ['Laptop', 'Smartphone', 'Tablet'],
#     'Price': [1200, 800, 400],
#     'Stock': [50, 150, 200]
# }

# df = pd.DataFrame(data)

# df["Category"] = "Electronics"

# df["New_Price"] = df["Price"] * 1.2

# df['Level'] = np.where(df['Price'] < 800, 'low', 'high')

# print(df)

# data = {
#     'Product': ['Laptop', 'Smartphone', 'Tablet'],
#     'Price': [1200.50, 800.75, 400.20],
#     'Stock': [50, 150, 200]
# }
# df = pd.DataFrame(data)
# df["Price"] = df["Price"].astype(int)
# print(df)

# data = {
#     'Event': ['Conference', 'Meeting', 'Workshop'],
#     'Date': ['2024-05-21', '2024-06-15', '2024-07-10']
# }

# data = {
#     'Name': ['Alex', 'Bella', 'Chris'],
#     'Age': [30, 25, 35],
#     'City': ['Kyiv', 'Lviv', 'Odesa']
# }
# # Перейменуйте стовпці 'Name' на 'Employee Name' та 'City' на 'Location'.

# df = pd.DataFrame(data)

# df.rename(columns=
#           {
#               "Name": "Employee Name",
#               'City': 'Location'
#           }, inplace=True)
# print(df)

# data = {
#     'Department': ['Sales', 'Engineering', 'Sales', 'HR', 'Engineering', 'HR', 'Sales'],
#     'Employee': ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace'],
#     'Salary': [70000, 80000, 75000, 60000, 82000, 58000, 72000],
#     'Region': ['North', 'South', 'North', 'East', 'South', 'East', 'West']
# }

# df = pd.DataFrame(data)
# grouped_data = df.groupby(['Department', 'Region'])
# agg = grouped_data.agg(
#     total_salary=("Salary", "sum"),
#     mean_salary=("Salary", "mean"),
#     employee_count=('Employee', "count"),
#     min_salary=("Salary", "min"),
#     max_salary=("Salary", "max"),
# )
# # print(agg)
# import matplotlib.pyplot as plt

# agg["mean_salary"].plot(kind="bar", color="skyblue")
# plt.show()

# df = pd.read_csv('2.csv')

# df['Date'] = pd.to_datetime(df['Date'])

# df['Temperature'] = pd.to_numeric(df['Temperature'], errors="coerce")

# df = df.dropna()

# df['Temperature'] = df['Temperature'].astype(int)

# print(df)

data = {
    'Department': ['Sales', 'Engineering', 'Sales', 'HR', 'Engineering', 'HR', 'Sales'],
    'Region': ['North', 'South', 'North', 'East', 'South', 'East', 'West'],
    'Sales': [1200, 1500, 800, 600, 1600, 750, 900],
    'Quantity': [10, 15, 8, 5, 20, 7, 9]
}
df = pd.DataFrame(data)
grouped_data = df.groupby(['Department', 'Region'])
agg = grouped_data.agg(
    
)