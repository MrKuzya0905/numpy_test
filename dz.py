import pandas as pd 
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import missingno as msno
from sklearn.impute import SimpleImputer

# Task 1

df = sns.load_dataset('tips')

sns.histplot(data=df, x='total_bill', bins=20, kde=True, hue='smoker')

plt.title('Розподіл Суми Рахунку за Категорією Курців')
plt.xlabel('Сума Рахунку (USD)')
plt.ylabel('Щільність Ймовірності')
plt.legend(title='Smoker')
plt.show()

# Task 2

df = sns.load_dataset('tips')

sns.histplot(
    data=df,
    x='total_bill',
    bins=20,
    kde=True,
    color='brown',
    alpha=0.7,
    kde_kws={'linewidth': 3}
)

plt.title('Розподіл Суми Рахунку з Налаштуваннями Графіка')
plt.xlabel('Сума Рахунку (USD)')
plt.ylabel('Щільність Ймовірності')
plt.show()

# Task 3

df = sns.load_dataset('penguins')
for col in df.select_dtypes(include='object').columns:
    df[col] = df[col].astype('category').cat.codes
corr = df.corr()
sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.title('Кореляційна Матриця (з урахуванням категорій)')
plt.show()