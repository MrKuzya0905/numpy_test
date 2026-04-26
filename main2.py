import pandas as pd 
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

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
from matplotlib.colors import LinearSegmentedColormap

df = sns.load_dataset('penguins')
df = df.select_dtypes(include=[int, float])
corr = df.corr()
colors = ["#ff0000", "#ffffff", "#0000ff"]
custom_cmap = LinearSegmentedColormap.from_list("CustomMap", colors, N=100)
sns.heatmap(corr, annot=True, cmap=custom_cmap, linewidths=0.5)
plt.title('Кореляційна Матриця з Власною Кольоровою Шкалою')
plt.show()