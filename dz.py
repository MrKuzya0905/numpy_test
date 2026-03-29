import numpy as np
# task1
# array1 = np.random.randint(-10, 11, (4, 4))
# array2 = np.random.randint(-10, 11, (4, 4))
# array3 = np.random.randint(-10, 11, (4, 4))


# combined_array = np.stack((array1, array2, array3))


# print("Об'єднаний масив з новою віссю:\n", combined_array)

# assert combined_array.shape == (3, 4, 4)

#task2
# B = np.random.randint(1, 10, (2, 3, 4))
# print("Оригінальний тривимірний масив B:\n", B)
# B_reshaped = B.reshape(6, 4)
# print("Масив після зміни форми:\n", B_reshaped)
# B_flattened = B.flatten()
# print("Одновимірний масив:\n", B_flattened)

#task3
C = np.random.randint(1, 10, (3, 3, 3))
print("Оригінальний масив C:\n", C)
sum_axis0 = np.sum(C, axis=0)
print("Сума по осі 0:\n", sum_axis0)
sum_axis1 = np.sum(C, axis=1)
print("Сума по осі 1:\n", sum_axis1)
total_sum = np.sum(C)
print("Загальна сума елементів масиву:", total_sum)