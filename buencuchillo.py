# # # #long
# # # matrix = [[0] * 3] *3
# # # print(matrix)
# # # #lc
# # # matrix = [[0] * 3 for i in range(3)]
# # # print(matrix)
# # # matrix [0][1] = 500
# # # print(matrix)
# # # #long
# # # numbers = []
# # # for i in range(3):
# # #     numbers.append(i)
# # # print(numbers)
# # # #LC
# # # numbers = [i for i in range(5)]
# # # print(numbers)
# #
# # values = []
# # for i in range(1,11):
# #     values.append(i + 5)
# # print(values)
# # #lc
# # values = [i + 5 for i in range(1,11)]
# # print(values)
# # #even
# # values = []
# # for i in range(1,11):
# #     if i % 2 == 0:
# #         values.append(i)
# # print(values)
# # #lc
# # values = [i for i in range(1,11) if i % 2 == 0]
# # print(values)
# # #long
# # numbers = [56, 78, 3 ,45, 1, 2]
# # tmp = []
# # for n in numbers:
# #     if n > 20:
# #         tmp.append(n)
# #     print(n)
# # #lc
# # tmp = [n for number in numbers if number > 20]
# # print(tmp)
# # #long multi dimensional
# # numbers = []
# # for row in range (3):
# #     curr_row = []
# #     for column in range(1, 6):
# #         curr_row.append(column)
# #     numbers.append(curr_row)
# #     print(numbers)
# # #LC
# # numbers = [[column for column in range(1, 6)] for row in range (3)]
# # print(numbers)
# # # long multiplication method
# # numbers = []
# # for row in range (1, 6):
# #     curr_row = []
# #     for column in range(1, 6):
# #         curr_row.append(row *  column)
# #     numbers.append(curr_row)
# # print(numbers)
# # #lc
# # numbers = [[row * column for column in range(1, 6)] for row in range (1, 6)]
# # print(numbers)
# # odd or even
# numbers = ["EVEN" if x % 2 == 0 else "ODD" for x in range(1, 11) ]
# print(numbers)
#
# values = [1,4,9,7]
# numbers = [[x for x in range(1,11) if x not in values] for i in range(5)]
# print(numbers)
# values = [1,4,9,7]
# numbers = [[x for x in range(10,0, -1) if x not in values] for i in range(5)]
# print(numbers)
# values = [1,4,9,7]
# numbers = [["x" if x % 2 == 0 else x for x in range(10,0, -1) ] for i in range(5)]
# print(numbers)
from os import linesep
from re import search


#INSERT
# numbers = [10, 20, 30]
# print(numbers)
# numbers.insert(1, 400)
# print(numbers)
#
# # extend
# numbers = [10, 20, 30]
# print(numbers)
# numbers.extend([33, 44, 55])
# print(numbers)
#
# #edit via range
# numbers = [10, 20, 30]
# print(numbers)
# numbers[1:5] = [44, 55, 66, 77]
# print(numbers)
#
# # remove
# numbers = [10, 20, 30]
# print(numbers)
# numbers.remove(30)
# print(numbers)
# numbers.remove(300) #error

#safe remove
def remove(lst, value):
    if value in lst:
        lst.remove(value)
    return lst

numbers = [10, 20, 30]
print(numbers)
numbers = remove(numbers, 300)
print(numbers)

# #pop
# numbers = [10, 20, 30,40 ,50, 60]
# print(numbers)
# x = numbers.pop(2)
# print(numbers, "the value of the index was: ", x)
# x = numbers.pop(2000) #error

#safe pop
# numbers = [10, 20, 30,40 ,50, 60]
# print(numbers)
# index_toPop = int(input("Enter the index you want to pop: "))
# x = numbers.pop(index_toPop) if index_toPop < len(numbers) else None
# print(numbers, "The value of the popped item was: ", x)
#del
# numbers = [10, 20, 30,40 ,50, 60]
# print(numbers)
# del numbers[1:5]
# print(numbers)
# #clear
# numbers = [10, 20, 30,40 ,50, 60]
# print(numbers)
# numbers.clear()
# print(numbers)
# # ---------------------------------------------
# #search
# numbers = [10, 20, 30, 40, 20 ,50, 60]
# print(numbers)
# position = numbers.index(20)
# print('30 was found in the index: ', position)
# position = numbers.index(20,3)
# print('20 was found in the index: ', position)
#split
# numbers = input('Enter a number: ').split(", ")
# print(numbers)

#get each word in a sentence
# sentence = "si sir jim na acsidente. Ahay!"
# words = [word for word in sentence.split(", ")]
# print(words)

# import random
# numbers = []
# random.randint(2,10)
# for i in range(5):
#     numbers.append(random.randint(2,10))
#     print(numbers)
# #lc version
# numbers = [random.randint(2,10) for x in range(5)]
# print(numbers)
# # -------------------------------------------------------------------
#
# print("Enter your love letter (Type 'Send') to send this to your sweetie: ")
# lines = []
# while True:
#     line = input()
#     if line == "SEND":
#         break
#     lines.append(line)
#     text = '\n'.join(lines)
# print(lines)
# print(text)

#mask passwords v1
# import msvcrt
# print('Enter password: ', end='', flush=True)
# password = ''
# while True:
#     ch =msvcrt.getwch()
#     if ch == '\r':
#         break
#     elif ch =='\b':
#         if password:
#             password = password[:-1]
#             print('\b \b', end='', flush=True)
#     else:
#         password += ch
#         print('@ ', end='', flush=True)
# print()
# print('Password: ', password)

#mask password part 2
from getpass import getpass
password = getpass('Enter Password')
print('Password: ', password)

#mask password v3 pip install
import pwinput
password = pwinput.password("Password", mask='@')
print('Password: ', password)