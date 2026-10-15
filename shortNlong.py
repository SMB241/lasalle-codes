import numpy as np
#traditional array loops
np1 = np.array([12,3,4,5,6])
for i in np1:
    print(i, end=' ')
print()
print('x' * 20)
#editing with nditer
np1 = np.array([[1,2,3,4],[5,6,7,8]])
for row in np1:
    for col in row:
        print(col, end='')
print()
print('x' * 20)
#editing with traditional loop
array = np.array([1,2,3],[4,5,6])
print(f'before:\n{array}')
for row in range(len(array)):
    for index, value in enumerate(array[row]):
        array[row, index] = 888
print(f'after:\n{array}')
print('x' * 20)
#editing using nditer loop
array = np.array([[1,2,3,4],[5,6,7,8]])
print(f'before:\n{array}')
for x in np.nditer(array, op_flags=['readwrite']):
    x[...]= 888
print(f'after:\n{array}')

#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

# comprehension
names = ['Jim', 'Bob', 'Tres']
nicknames = ['Boy', 'bie', 'ly']
ages = [25, 30, 35]

combined_info = [f'{name}{nickname} is {age}yrs. old'
                 for name, nickname, age in zip(names, nicknames, ages)]

print(combined_info, type(combined_info))

mynumpy_combined = np.array(combined_info)
print(mynumpy_combined, type(mynumpy_combined))

# ask for ID, (name, gender) (NUMPY)
Stud_ID = np.array([], dtype=int)
Stud_details = np.empty((0, 2), dtype=object)

while True:
    stud_id = input('Enter Student ID (press X to stop):')
    if stud_id.lower() == 'x':
        break

    stud_name = input('Enter Student name:')
    stud_gender = input('Enter Student gender:')

    # append to Stud_ID and Stud_details
    Stud_ID = np.append(Stud_ID, int(stud_id))
    tmp = np.array([[stud_name, stud_gender]], dtype=object)
    Stud_details = np.append(Stud_details, tmp, axis=0)

# Join the 2 different arrays together Stud_ID, Stud_details
Final = np.empty((len(Stud_ID), 3), dtype=object)
Final[:, 0] = Stud_ID
Final[:, 1:] = Stud_details

print('-STUDENTS LIST-')
for value in Final:
    print(f'StudentID: {value[0]}')
    print(f'name: {value[1]}')
    print(f'gender: {value[2]}')

print('-NOTHING FOLLOWS-')

#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
#quiz
import numpy as np

txt = input("Enter E if you want to encrypt or D if you want to Decrypt: ")

np1 = np.array(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm'])
np2 = np.array(['n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'])

pairs = dict(zip(np1, np2))

vowels = {'a': '!', 'e': '#', 'i': '$', 'o': '%', 'u': '&'}

mapping = {}

for a, b in pairs.items():
    mapping[a] = b
    mapping[b] = a


def encrypt(txt):
