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

B = np.array([
    [10, 20, 30, 40],
    [50, 60, 70, 80],
    [90, 100, 110, 120],
    [130, 140, 150, 160]
])

print(B[0:2, 0:2])