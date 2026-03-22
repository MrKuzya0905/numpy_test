import numpy as np

arr1 = np.arange(10, 20)

print("Завдання 1:")
print("Масив:", arr1)
print("Сума:", np.sum(arr1))
print("Середнє:", np.mean(arr1))
print("Мін:", np.min(arr1))
print("Макс:", np.max(arr1))


arr2 = np.random.rand(1000)  
print("\nЗавдання 2:")
print("Сума:", np.sum(arr2))
print("Середнє:", np.mean(arr2))
print("Мін:", np.min(arr2))
print("Макс:", np.max(arr2))


arr3 = np.random.randint(0, 100, (5, 5))

print("\nЗавдання 3:")
print("Масив:\n", arr3)


print("Другий стовпець:", arr3[:, 1])

print("Другий рядок:", arr3[1, :])


flattened = arr3.flatten()
print("Одномірний масив:", flattened)



arr4 = np.random.rand(500000)

print("\nЗавдання 4:")
print("Сума:", np.sum(arr4))
print("Середнє:", np.mean(arr4))
print("Мін:", np.min(arr4))
print("Макс:", np.max(arr4))