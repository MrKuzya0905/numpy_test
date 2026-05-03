import pandas as pd 
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import missingno as msno
from sklearn.impute import SimpleImputer

# tips = sns.load_dataset("tips")
# sns.histplot(data=tips, x="total_bill")
# plt.show()

# data = {
#     'Date': [
#         '2023-01-01', '2023-01-01', '2023-01-02', '2023-01-02', '2023-01-03',
#         '2023-01-04', '2023-01-04', '2023-01-05', '2023-01-05', '2023-01-06',
#         '2023-02-01', '2023-02-01', '2023-02-02', '2023-02-02', '2023-02-03',
#         '2023-02-04', '2023-02-04', '2023-02-05', '2023-02-05', '2023-02-06'
#     ],
#     'Product': [
#         'Smartphone', 'Laptop', 'Tablet', 'Headphones', 'Smartwatch',
#         'Smartphone', 'Laptop', 'Tablet', 'Headphones', 'Smartwatch',
#         'Smartphone', 'Laptop', 'Tablet', 'Headphones', 'Smartwatch',
#         'Smartphone', 'Laptop', 'Tablet', 'Headphones', 'Smartwatch'
#     ],
#     'Category': [
#         'Mobile Devices', 'Computers', 'Mobile Devices', 'Accessories', 'Accessories',
#         'Mobile Devices', 'Computers', 'Mobile Devices', 'Accessories', 'Accessories',
#         'Mobile Devices', 'Computers', 'Mobile Devices', 'Accessories', 'Accessories',
#         'Mobile Devices', 'Computers', 'Mobile Devices', 'Accessories', 'Accessories'
#     ],
#     'Region': [
#         'North', 'South', 'East', 'West', 'North',
#         'South', 'East', 'West', 'North', 'South',
#         'East', 'West', 'North', 'South', 'East',
#         'West', 'North', 'South', 'East', 'West'
#     ],
#     'Sales': [
#         50, 30, 20, 100, 40,
#         60, 25, 35, 80, 45,
#         55, 40, 25, 90, 50,
#         65, 35, 30, 100, 55
#     ],
#     'Revenue': [
#         25000, 45000, 10000, 10000, 20000,
#         30000, 37500, 17500, 8000, 22500,
#         27500, 60000, 12500, 9000, 25000,
#         32500, 52500, 15000, 10000, 27500
#     ]
# }
# data = {
#     'Date': [
#         '2023-01-01', '2023-01-01', '2023-01-02', '2023-01-02', '2023-01-03',
#         '2023-01-04', '2023-01-04', '2023-01-05', '2023-01-05', '2023-01-06',
#         '2023-02-01', '2023-02-01', '2023-02-02', '2023-02-02', '2023-02-03',
#         '2023-02-04', '2023-02-04', '2023-02-05', '2023-02-05', '2023-02-06'
#     ],
#     'Product': [
#         'Smartphone', 'Laptop', 'Tablet', 'Headphones', 'Smartwatch',
#         'Smartphone', 'Laptop', 'Tablet', 'Headphones', 'Smartwatch',
#         'Smartphone', 'Laptop', 'Tablet', 'Headphones', 'Smartwatch',
#         'Smartphone', 'Laptop', 'Tablet', 'Headphones', 'Smartwatch'
#     ],
#     'Category': [
#         'Mobile Devices', 'Computers', 'Mobile Devices', 'Accessories', 'Accessories',
#         'Mobile Devices', 'Computers', 'Mobile Devices', 'Accessories', 'Accessories',
#         'Mobile Devices', 'Computers', 'Mobile Devices', 'Accessories', 'Accessories',
#         'Mobile Devices', 'Computers', 'Mobile Devices', 'Accessories', 'Accessories'
#     ],
#     'Region': [
#         'North', 'South', 'East', 'West', 'North',
#         'South', 'East', 'West', 'North', 'South',
#         'East', 'West', 'North', 'South', 'East',
#         'West', 'North', 'South', 'East', 'West'
#     ],
#     'Sales': [
#         50, 30, 20, 100, 40,
#         60, 25, 35, 80, 45,
#         55, 40, 25, 90, 50,
#         65, 35, 30, 100, 55
#     ],
#     'Revenue': [
#         25000, 45000, 10000, 10000, 20000,
#         30000, 37500, 17500, 8000, 22500,
#         27500, 60000, 12500, 9000, 25000,
#         32500, 52500, 15000, 10000, 27500
#     ]
# }
# df = pd.DataFrame(data)

# # sns.countplot(x=None, y=None, hue=None, data=None, order=None, hue_order=None,
# #               orient=None, color=None, palette=None, saturation=0.75, dodge=True, ax=None, **kwargs)

# sns.countplot(data=df, x="Category", palette="Set2", hue="Category", legend=False)
# plt.xlabel("category")
# plt.ylabel("sales")
# plt.show()


# tips = sns.load_dataset("tips")

# sns.barplot(
#     data=tips,
#     x="day",
#     y="total_bill",
#     hue="time",
#     palette="deep"
# )
# plt.title("Середній рахунок за днями тижня")
# plt.xlabel("День тижня")
# plt.ylabel("Сума рахунку")
# plt.legend(title="Час Прийому Їжі")
# plt.show()

# tips = sns.load_dataset("tips")

# sns.barplot(
#     data=tips,
#     x="day",
#     y="total_bill",
#     estimator=np.sum,
#     palette="coolwarm"
# )

# plt.title("Загальна сума рахунків за днями тижня")
# plt.xlabel("День тижня")
# plt.ylabel("Сума рахунків")
# plt.show()


# df = sns.load_dataset("penguins")
# # sns.barplot(data=df, x="species", y="body_mass_g", palette="Set2", hue="sex", legend=False)
# # plt.show()

# sns.kdeplot(df, hist=True, kde=True)
# plt.xlabel("Mass")
# plt.ylabel("Count")
# plt.show()

# df = sns.load_dataset('tips')
# sns.distplot(df['total_bill'], bins=20, kde=False, color='blue', rug=True)
# plt.title('Розподіл Суми Рахунку')
# plt.xlabel('Сума Рахунку (USD)')
# plt.ylabel('Кількість Спостережень')
# plt.show()

# df = sns.load_dataset('tips')
# sns.distplot(df['total_bill'], bins=25, kde=True, color='green')
# plt.title('Розподіл Суми Рахунку з KDE')
# plt.xlabel('Сума Рахунку (USD)')
# plt.ylabel('Щільність Ймовірності')
# plt.show()
# from matplotlib.colors import LinearSegmentedColormap

# df = sns.load_dataset('penguins')
# df = df.select_dtypes(include=[int, float])
# corr = df.corr()
# colors = ["#ff0000", "#ffffff", "#0000ff"]
# custom_cmap = LinearSegmentedColormap.from_list("CustomMap", colors, N=100)
# sns.heatmap(corr, annot=True, cmap=custom_cmap, linewidths=0.5)
# plt.title('Кореляційна Матриця з Власною Кольоровою Шкалою')
# plt.show()

# df = pd.read_csv("data.csv")
# # # print(df.isnull().count)
# # msno.matrix(df, figsize=(12, 8))
# # median_val = df["Salary"].median()
# df["Age"] = df["Age"].ffill(inplace=True)
# print(df)

# url = 'https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv'
# df = pd.read_csv(url)

# df = pd.read_csv('data.csv')
# missing_values = df.isnull().sum()

# print(missing_values)
# df = pd.read_csv('data.csv')
# median_salary = df['Salary'].median()

# df['Salary'] = df['Salary'].fillna(median_salary)

# print(df['Salary'].head())
# pd.DataFrame.replace(to_replace, value, inplace=False, limit=None, regex=False, method='pad')
# pd.DataFrame.replace({"to_replace": "value"})
# pd.DataFrame("^\+380\d{9}$", "phone_number", regex=True)

# data = {'Status': ['Single', 'Married', 'Single', 'Divorced']}
# df = pd.DataFrame(data)
# df.replace({
#     "Single": 1,
#     "Married": 2,
#     "Divorced": 3
# }, inplace=True)
# print(df)

# data = {'Comments': ['Good product', 'bad quality', 'average', 'excellent']}
# df = pd.DataFrame(data)
# df.replace("^bad.+", "poor", inplace=True, regex=True)
# print(df)

# df1 = pd.DataFrame({
#     'A': ['A0', 'A1', 'A2'],
#     'B': ['B0', 'B1', 'B2']
# })
# df2 = pd.DataFrame({
#     'C': ['C0', 'C1', 'C2'],
#     'D': ['D0', 'D1', 'D2']
# })
# df = pd.concat([df1, df2], axis=1)
# print(df)

# df1 = pd.DataFrame({
#     'ProductID': [1, 2, 3],
#     'Category': ['Electronics', 'Home Appliances', 'Electronics'],
#     'Price': [699, 1200, 850]
# })
# df2 = pd.DataFrame({
#     'ProductID': [4, 5],
#     'Category': ['Furniture', 'Electronics'],
#     'Price': [500, 650]
# })
# df = pd.concat([df1, df2], axis=0, ignore_index=False)
# print(df)

# df1 = pd.DataFrame({
#     'ProductID': [1, 2, 3],
#     'Category': ['Electronics', 'Home Appliances', 'Electronics']
# })
# df2 = pd.DataFrame({
#     'Price': [699, 1200, 850],
#     'Availability': ['In Stock', 'Out of Stock', 'In Stock']
# })
# df = pd.concat([df1, df2], axis=1)
# print(df)

# df1 = pd.DataFrame({
#     'ProductID': [1, 2, 3],
#     'Category': ['Electronics', 'Home Appliances', 'Electronics']
# })
# df2 = pd.DataFrame({
#     'ProductID': [4, 5],
#     'Price': [500, 650]
# })
# df = pd.concat([df1, df2], axis=0, join="outer")
# print(df)

sales_q1 = pd.DataFrame({
    'ProductID': [101, 102, 103],
    'Sales': [250, 150, 300]
})
sales_q2 = pd.DataFrame({
    'ProductID': [104, 105],
    'Sales': [200, 350]
})
result = pd.concat([sales_q1, sales_q2], axis=0, ignore_index=True)
print(result)

df1 = pd.DataFrame({
    'EmployeeID': [1, 2, 3],
    'Name': ['Alice', 'Bob', 'Charlie']
})
df2 = pd.DataFrame({
    'EmployeeID': [4, 5],
    'Name': ['David', 'Eva']
})
result = pd.concat([df1, df2], axis=0, ignore_index=True)
print(result)