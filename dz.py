import numpy as np
import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt

# Task 1

weeks = ['Тиждень 1', 'Тиждень 2', 'Тиждень 3', 'Тиждень 4']

traffic = [1500, 1600, 1700, 1800]

sales_product_a = [300, 350, 400, 450]
sales_product_b = [200, 250, 300, 350]
sales_product_c = [100, 150, 200, 250]

plt.figure(figsize=(10, 6))
plt.plot(weeks, traffic, label='Трафік', linestyle='-', marker='o')
plt.plot(weeks, sales_product_a, label='Продукт A', linestyle='--', marker='s')
plt.plot(weeks, sales_product_b, label='Продукт B', linestyle='-.', marker='^')
plt.plot(weeks, sales_product_c, label='Продукт C', linestyle=':', marker='d')

plt.title('Щотижнева активність трафіку та продажів')
plt.xlabel('Тижні')
plt.ylabel('Кількість')
plt.legend()
plt.grid()

plt.show()

# Task 2

x = np.linspace(0, 10, 1000)
y = np.sin(x) * np.cos(x)

plt.figure(figsize=(12, 6))
plt.plot(x, y)

plt.title('Графік функції y = sin(x) * cos(x)')
plt.xlabel('x')
plt.ylabel('y')

plt.tight_layout()
plt.show()

# Task 3

sizes = [50, 25, 15, 10]
labels = ['Продажі', 'Інвестиції', 'Ліцензії', 'Інше']

plt.pie(
    sizes,
    labels=labels,
    colors=['#FF9999', '#66B3FF', '#99FF99', '#FFCC99']
)

plt.title("Кольори сегментів")
plt.show()