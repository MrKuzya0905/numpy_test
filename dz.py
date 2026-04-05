import numpy as np


# Завдання 1

array = np.array([12, -5, 7, 9, -3, 15])
array_new = np.append(array, 10)
print(array_new)



# Завдання 2

matrix = np.array([
    [5, 2, 8],
    [1, 7, 4],
    [3, 6, 9]
])

matrix_new = np.delete(matrix, 1, axis=0)
print(matrix_new)



# Завдання 3
conversions = np.array([50, 65, 80, 45, 70, 90, 55, 85, 60, 75])

print("\nЗавдання 3:")
print("Масив:", conversions)


median = np.median(conversions)
variance = np.var(conversions)
std_dev = np.std(conversions)

print("Медіана:", median)
print("Дисперсія:", variance)
print("Стандартне відхилення:", std_dev)


uniform = np.random.uniform(0, 100, 10)   
integers = np.random.randint(0, 100, 10)    
real = np.random.rand(10) * 100            
normal = np.random.normal(50, 10, 10)       

combined = np.concatenate([conversions, uniform, integers, real, normal])

mean_value = np.mean(combined)

print("Середнє значення:", mean_value)

if mean_value > 2000:
    print("Середнє більше за 2000")
else:
    print("Середнє НЕ більше за 2000")