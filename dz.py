import pandas as pd 
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import missingno as msno
from sklearn.impute import SimpleImputer
import time

# Завдання 1

df_a = pd.DataFrame({
    'EmployeeID': [1, 2, 3],
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Department': ['HR', 'Engineering', 'Marketing']
})

df_b = pd.DataFrame({
    'EmployeeID': [4, 5],
    'Name': ['David', 'Eva'],
    'Department': ['Finance', 'IT']
})

combined_df = pd.concat(
    [df_a, df_b],
    ignore_index=True,
    keys=['Group_A', 'Group_B']
)

print(combined_df)

# Завдання 2

orders_df = pd.DataFrame({
    'OrderID': [1001, 1002, 1003, 1004],
    'CustomerID': [1, 2, 1, 3],
    'ProductID': [501, 502, 503, 504],
    'Quantity': [2, 1, 5, 3]
})

customers_df = pd.DataFrame({
    'CustomerID': [1, 2, 3, 4],
    'CustomerName': ['Alice', 'Bob', 'Charlie', 'David']
})

customer_products_df = pd.DataFrame({
    'CustomerID': [1, 2, 3],
    'ProductID': [501, 502, 504],
    'Category': ['Electronics', 'Office', 'Home']
})

merged_df = pd.merge(
    orders_df,
    customer_products_df,
    on=['CustomerID', 'ProductID'],
    how='inner',
    indicator=True
)

print(merged_df)

# Завдання 3

np.random.seed(0)

transactions_df = pd.DataFrame({
    'TransactionID': range(1, 100001),
    'UserID': np.random.randint(1, 1001, size=100000),
    'ProductID': np.random.randint(1, 500, size=100000),
    'Date': pd.date_range(start='2023-01-01', periods=100000, freq='min'),
    'Amount': np.random.uniform(10.0, 1000.0, size=100000)
})

products_df = pd.DataFrame({
    'ProductID': range(1, 500),
    'ProductName': [f'Product_{i}' for i in range(1, 500)]
})

transactions_df['Amount'] = transactions_df['Amount'].astype('float32')

transactions_optimized = transactions_df.set_index(['UserID', 'ProductID'])

start_time = time.time()

merge_normal = pd.merge(
    transactions_df,
    products_df,
    on='ProductID'
)

normal_time = time.time() - start_time

products_indexed = products_df.set_index('ProductID')

start_time = time.time()

merge_optimized = transactions_optimized.join(
    products_indexed,
    on='ProductID'
)

optimized_time = time.time() - start_time

print("Час без оптимізації:", normal_time)
print("Час з оптимізацією:", optimized_time)

# Завдання 4

df_sales = pd.DataFrame({
    'SaleID': [2001, 2002, 2003, 2004, 2005],
    'StoreID': [10, 20, 10, 30, 20],
    'ProductID': [301, 302, 303, 301, 304],
    'UnitsSold': [50, 60, 70, 80, 90]
})

df_suppliers = pd.DataFrame({
    'SupplierID': [401, 402, 403, 404],
    'ProductID': [301, 302, 303, 305],
    'SupplierName': ['Supplier A', 'Supplier B', 'Supplier C', 'Supplier D']
})

df_sales_optimized = df_sales.set_index(['StoreID', 'ProductID'])

merged_sales = pd.merge(
    df_sales,
    df_suppliers,
    on='ProductID',
    how='left',
    validate='many_to_one',
    suffixes=('_sales', '_supplier')
)

print(merged_sales)