import numpy as np

# array = np.arange(1000, 10**6)
# print(array * 5)


# image = Image.open("image.jpg")
# matrix = np.array(image)
# matrix_plus = matrix + 50
# matrix_plus = np.clip(matrix_plus, 0, 255)
# image_plus = Image.fromarray(matrix_plus)
# image_plus.save("image_plus.jpg")

# from sklearn.linear_model import LinearRegression

# x = [[1],[2],[3],[4]]
# y = [[2],[4],[6],[8]]

# model = LinearRegression()
# model.fit(x,y)
# prediction = model.predict([[7]])
# print(prediction)
# import time

# start = time.time()
# my_list = list(range(10**6))
# sum_list = sum(my_list)
# print(sum_list)
# print(f"List time = {time.time() - start}")

# start = time.time()
# array = np.arange(10**6)
# sum_array = np.sum(array)
# print(sum_array)
# print(f"Array time = {time.time() - start}")

# matrix = [
#     [2, 4, 6],
#     [8, 10, 12],
#     [14, 16, 18]
# ]

# array = np.array(matrix)
# sum_array = np.sum(matrix)
# print(array)
# print(sum_array)

# ones = np.ones((1, 3))
# new_matrix = np.concatenate(array, ones)
# print(new_matrix)


# array1 = np.arange(0, 9999, dtype=np.int64)
# array2 = np.arange(0, 9999, dtype=np.int16)
# print(array1.nbytes)
# print(array2.nbytes)


# arr = np.arange(1, 17).reshape(4, 4)
# arr = np.where(arr % 3 == 0, -1, arr)
# print(arr)

# array1 = np.array([[1],
#                    [2],
#                    [3]])
# array2 = np.array([[4],
#                    [5],
#                    [6]])

# array = np.dstack((array1, array2))
# print(array)

# B = np.array([
#     [10, 20, 30, 40],
#     [50, 60, 70, 80],
#     [90, 100, 110, 120],
#     [130, 140, 150, 160]
# ])

# print(B[0:2, 0:2])

# arr = np.array([10, 20, 30, 40, 50, 60])

# arr1 = np.delete(arr, 2)
# print("Після видалення індексу 2:", arr1)

# arr2 = np.delete(arr, [0, 3, 4])
# print("Після видалення індексів 0, 3, 4:", arr2)

# arr = np.random.randint(1, 21, 10)
# print("Початковий масив:", arr)

# indices = np.where(arr % 3 == 0)

# new_arr = np.delete(arr, indices)

# print("Масив без чисел, що діляться на 3:", new_arr)

# Створіть двовимірний масив NumPy розміром 4x5 з
# випадкових цілих чисел від 0 до 50.
# Видаліть другий рядок та четвертий стовпець з цього масиву.
# Виведіть отриманий масив.

# arr = np.random.randint(0, 51, size=(4, 5))
# print("Початковий масив:\n", arr)

# arr = np.delete(arr, 1, axis=0)

# arr = np.delete(arr, 3, axis=1)

# print("\nОновлений масив:\n", arr)

# arr = np.random.randint(1, 101, 20)
# print("Початковий масив:")
# print(arr)

# unique_arr = []
# for x in arr:
#     if x not in unique_arr:
#         unique_arr.append(x)

# unique_arr = np.array(unique_arr)

# print("Масив без повторів:")
# print(unique_arr)

A = np.array([[1, 4, 7],
              [2, 5, 8],
              [3, 6, 9]])
B = np.array([[9, 6, 3],
              [8, 5, 2],
              [7, 4, 1]])

AB = np.dot(A, B)
BA = np.dot(B, A)

print("A * B:")
print(AB)

print("\nB * A:")
print(BA)

try:
    A_inv = np.linalg.inv(A)
    print("\nОбернена матриця A:")
    print(A_inv)
except np.linalg.LinAlgError:
    print("\nМатриця A не має оберненої (вироджена)")

try:
    B_inv = np.linalg.inv(B)
    print("\nОбернена матриця B:")
    print(B_inv)
except np.linalg.LinAlgError:
    print("\nМатриця B не має оберненої (вироджена)")

print(A @ B)
print(B @ A)