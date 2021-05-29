import numpy as np

# arr = np.array([[5, 10, 15], [20, 25, 30], [35, 40, 45]])

# print(arr)
# print(arr[2,1])
# print(arr[1:, 1:][0])

# # # comma notation doesn't work for ordinary python list
# # norm_arr = [[5, 10, 15], [20, 25, 30], [35, 40, 45]]
# # print(norm_arr)
# # print(norm_arr[2][1])

# bool_arr = arr > 25
# print(bool_arr)

# big_array = np.arange(50).reshape(5,10)
# new_arr = np.zeros((5,10))
# new_arr[big_array % 2 != 0] = 1
# print(big_array)
# print(big_array[1:3, 3:5])
# print(big_array[1:,3:][:2, :2])

print(np.arange(1, 101).reshape(10, 10) / 100)
print(np.linspace(0, 1, 20))

mat = np.arange(1, 26).reshape(5, 5)
print(mat)
print(mat[:, 1:][:3, :1])
print(mat[-2:])

print(np.sum(mat, axis=0))
