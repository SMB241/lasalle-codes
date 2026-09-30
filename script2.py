import numpy as np

np.set_printoptions(precision=2, threshold=np.inf, suppress=True)

arr = np.array([
    [1000, 4534, 222, 5465, 12345678.123456789],
    [444, 555, 666]
])

print(arr)

print('--------------------')

arr[1, 0] = 888

print(arr)


import numpy as np

np1 = np.array([1, 2, 3, -4, 0, 5, 6, 7, -8, 9])

print(np.absolute(np1))

print(np.exp(np1))

print(np.min(np1))

print(np.max(np1))

print(np.sign(np1))


import numpy as np

arr = np.array([1, 2, 3])

new_arr = np.append(arr, [4, 5, 6])

print(new_arr)

arr = np.array([[1, 2, 3], [4, 5, 6]])

new_arr = np.append(arr, [[7, 8, 9]], axis=0)

print(new_arr)

print('--------------------')

arr = np.array([[1, 2, 3], [4, 5, 6]])

print(arr)

new_arr = np.append(arr, [[7], [8]], axis=1)

print(new_arr)

arr = np.array([1, 2, [3, 4]])

print(arr)

print('--------------------')

arr = np.append(arr, [5, 6])

print(arr)

arr = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

arr = np.array([[1, 2], [3, 4]])

rows = [[5, 6], [7, 8]]

print(arr)

print('--------------------')

new_arr = np.append(arr, rows, axis=0)

print(new_arr)

arr = np.delete(arr, 1, axis=0)

arr = np.array([
    [10, 20],
    [30, 40],
    [50, 60],
    [70, 80]
])

new_arr = np.delete(arr, np.s_[::2], axis=0)

import numpy as np

np.set_printoptions(precision=2, threshold=np.inf, suppress=True)

arr = np.array([
    [1000, 4534, 222, 5465, 12345678.123456789],
    [444, 555, 666]
])

print(arr)

print('--------------------')

arr[1, 0] = 888

print(arr)


import numpy as np

np1 = np.array([1, 2, 3, -4, 0, 5, 6, 7, -8, 9])

print(np.absolute(np1))

print(np.exp(np1))

print(np.min(np1))

print(np.max(np1))

print(np.sign(np1))


import numpy as np

arr = np.array([1, 2, 3])

new_arr = np.append(arr, [4, 5, 6])

print(new_arr)

arr = np.array([[1, 2, 3], [4, 5, 6]])

new_arr = np.append(arr, [[7, 8, 9]], axis=0)

print(new_arr)

print('--------------------')

arr = np.array([[1, 2, 3], [4, 5, 6]])

print(arr)

new_arr = np.append(arr, [[7], [8]], axis=1)

print(new_arr)

arr = np.array([1, 2, [3, 4]])

print(arr)

print('--------------------')

arr = np.append(arr, [5, 6])

print(arr)

arr = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

arr = np.array([[1, 2], [3, 4]])

rows = [[5, 6], [7, 8]]

print(arr)

print('--------------------')

new_arr = np.append(arr, rows, axis=0)

print(new_arr)

arr = np.delete(arr, 1, axis=0)

arr = np.array([
    [10, 20],
    [30, 40],
    [50, 60],
    [70, 80]
])

new_arr = np.delete(arr, np.s_[::2], axis=0)

print(np3)

print(np3.shape)

print('----------------------------------')

np5 = np4.flatten()

print(np5)

print(np5.shape)


import numpy as np

grocery_dtype = np.dtype([
    ('item_name', 'U10'),
    ('product_code', 'U5'),
    ('qty', 'i4'),
    ('price', 'f4')
])

grocery_data = np.array([
    ('Apple', 'A101', 40, 50.60),
    ('Grapes', 'G102', 30, 125.00),
    ('Oranges', 'O103', 90, 60.02),
    ('Bananas', 'B104', 100, 10.75)
], dtype=grocery_dtype)

print(grocery_data)

print(grocery_data[0])

print(grocery_data[1])

print(grocery_data[2])

second_row_first_three_columns = grocery_data[1][['item_name', 'product_code', 'qty']]

print('\n', second_row_first_three_columns)

grocery_data[0]['item_name'] = 'XXX'

grocery_data[1]['product_code'] = 'X105'

grocery_data[1]['qty'] = 88

print(grocery_data)

print('----------------------------------')

grocery_data = np.delete(grocery_data, 1, axis=0)

print(grocery_data)