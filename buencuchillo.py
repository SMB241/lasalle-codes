# # # # # #long
# # # # # matrix = [[0] * 3] *3
# # # # # print(matrix)
# # # # # #lc
# # # # # matrix = [[0] * 3 for i in range(3)]
# # # # # print(matrix)
# # # # # matrix [0][1] = 500
# # # # # print(matrix)
# # # # # #long
# # # # # numbers = []
# # # # # for i in range(3):
# # # # #     numbers.append(i)
# # # # # print(numbers)
# # # # # #LC
# # # # # numbers = [i for i in range(5)]
# # # # # print(numbers)
# # # #
# # # # values = []
# # # # for i in range(1,11):
# # # #     values.append(i + 5)
# # # # print(values)
# # # # #lc
# # # # values = [i + 5 for i in range(1,11)]
# # # # print(values)
# # # # #even
# # # # values = []
# # # # for i in range(1,11):
# # # #     if i % 2 == 0:
# # # #         values.append(i)
# # # # print(values)
# # # # #lc
# # # # values = [i for i in range(1,11) if i % 2 == 0]
# # # # print(values)
# # # # #long
# # # # numbers = [56, 78, 3 ,45, 1, 2]
# # # # tmp = []
# # # # for n in numbers:
# # # #     if n > 20:
# # # #         tmp.append(n)
# # # #     print(n)
# # # # #lc
# # # # tmp = [n for number in numbers if number > 20]
# # # # print(tmp)
# # # # #long multi dimensional
# # # # numbers = []
# # # # for row in range (3):
# # # #     curr_row = []
# # # #     for column in range(1, 6):
# # # #         curr_row.append(column)
# # # #     numbers.append(curr_row)
# # # #     print(numbers)
# # # # #LC
# # # # numbers = [[column for column in range(1, 6)] for row in range (3)]
# # # # print(numbers)
# # # # # long multiplication method
# # # # numbers = []
# # # # for row in range (1, 6):
# # # #     curr_row = []
# # # #     for column in range(1, 6):
# # # #         curr_row.append(row *  column)
# # # #     numbers.append(curr_row)
# # # # print(numbers)
# # # # #lc
# # # # numbers = [[row * column for column in range(1, 6)] for row in range (1, 6)]
# # # # print(numbers)
# # # # odd or even
# # # numbers = ["EVEN" if x % 2 == 0 else "ODD" for x in range(1, 11) ]
# # # print(numbers)
# # #
# # # values = [1,4,9,7]
# # # numbers = [[x for x in range(1,11) if x not in values] for i in range(5)]
# # # print(numbers)
# # # values = [1,4,9,7]
# # # numbers = [[x for x in range(10,0, -1) if x not in values] for i in range(5)]
# # # print(numbers)
# # # values = [1,4,9,7]
# # # numbers = [["x" if x % 2 == 0 else x for x in range(10,0, -1) ] for i in range(5)]
# # # print(numbers)
# # from os import linesep
# # from re import search
# #
# #
# # #INSERT
# # # numbers = [10, 20, 30]
# # # print(numbers)
# # # numbers.insert(1, 400)
# # # print(numbers)
# # #
# # # # extend
# # # numbers = [10, 20, 30]
# # # print(numbers)
# # # numbers.extend([33, 44, 55])
# # # print(numbers)
# # #
# # # #edit via range
# # # numbers = [10, 20, 30]
# # # print(numbers)
# # # numbers[1:5] = [44, 55, 66, 77]
# # # print(numbers)
# # #
# # # # remove
# # # numbers = [10, 20, 30]
# # # print(numbers)
# # # numbers.remove(30)
# # # print(numbers)
# # # numbers.remove(300) #error
# #
# # #safe remove
# # def remove(lst, value):
# #     if value in lst:
# #         lst.remove(value)
# #     return lst
# #
# # numbers = [10, 20, 30]
# # print(numbers)
# # numbers = remove(numbers, 300)
# # print(numbers)
# #
# # # #pop
# # # numbers = [10, 20, 30,40 ,50, 60]
# # # print(numbers)
# # # x = numbers.pop(2)
# # # print(numbers, "the value of the index was: ", x)
# # # x = numbers.pop(2000) #error
# #
# # #safe pop
# # # numbers = [10, 20, 30,40 ,50, 60]
# # # print(numbers)
# # # index_toPop = int(input("Enter the index you want to pop: "))
# # # x = numbers.pop(index_toPop) if index_toPop < len(numbers) else None
# # # print(numbers, "The value of the popped item was: ", x)
# # #del
# # # numbers = [10, 20, 30,40 ,50, 60]
# # # print(numbers)
# # # del numbers[1:5]
# # # print(numbers)
# # # #clear
# # # numbers = [10, 20, 30,40 ,50, 60]
# # # print(numbers)
# # # numbers.clear()
# # # print(numbers)
# # # # ---------------------------------------------
# # # #search
# # # numbers = [10, 20, 30, 40, 20 ,50, 60]
# # # print(numbers)
# # # position = numbers.index(20)
# # # print('30 was found in the index: ', position)
# # # position = numbers.index(20,3)
# # # print('20 was found in the index: ', position)
# # #split
# # # numbers = input('Enter a number: ').split(", ")
# # # print(numbers)
# #
# # #get each word in a sentence
# # # sentence = "si sir jim na acsidente. Ahay!"
# # # words = [word for word in sentence.split(", ")]
# # # print(words)
# #
# # # import random
# # # numbers = []
# # # random.randint(2,10)
# # # for i in range(5):
# # #     numbers.append(random.randint(2,10))
# # #     print(numbers)
# # # #lc version
# # # numbers = [random.randint(2,10) for x in range(5)]
# # # print(numbers)
# # # # -------------------------------------------------------------------
# # #
# # # print("Enter your love letter (Type 'Send') to send this to your sweetie: ")
# # # lines = []
# # # while True:
# # #     line = input()
# # #     if line == "SEND":
# # #         break
# # #     lines.append(line)
# # #     text = '\n'.join(lines)
# # # print(lines)
# # # print(text)
# #
# # #mask passwords v1
# # # import msvcrt
# # # print('Enter password: ', end='', flush=True)
# # # password = ''
# # # while True:
# # #     ch =msvcrt.getwch()
# # #     if ch == '\r':
# # #         break
# # #     elif ch =='\b':
# # #         if password:
# # #             password = password[:-1]
# # #             print('\b \b', end='', flush=True)
# # #     else:
# # #         password += ch
# # #         print('@ ', end='', flush=True)
# # # print()
# # # print('Password: ', password)
# #
# # #mask password part 2
# # from getpass import getpass
# # password = getpass('Enter Password')
# # print('Password: ', password)
# #
# # #mask password v3 pip install
# # import pwinput
# # password = pwinput.password("Password", mask='@')
# # print('Password: ', password)
# #
#
# input = int(input('Enter the size of the board: '))
# board = [[column for column in range(1, input+ 1)] for row in range (input)]
# print(board, end=" ")
#
# for row in range(1, input):
#     for column in range(1, input):
#         print(board[row][column], end=" ")
#
# board = [[column for column in range(1, size + 1)] for row in range (1, size + 1)]
# print(board, end=" ")
#
#
from tkinter.font import names

from py import numbers

#keywords
# def greet_person(name, person):
#     print("Hello, ", name + ", ", person)
# greet_person("Garde", "C")
# greet_person(section='A',name='Sison')

#ARGS
# def solve(num1, num2):
#     sum = num1 + num2
#     return sum
# #calling the function
# print(solve(1, 2))
#Args
# def solve2(*numbers):
#     print(numbers)
#     total = 0
#     for num in numbers:
#         total += num
#         print(total)
# #call the 2nd function
# print(solve2(1, 2, 3, 4, 5))
#KWARGS **
# function that returns many values
# def compute(n1, n2):
#     add = n1 + n2
#     sub = n1 - n2
#     mult = n1 * n2
#     div = n1 / n2
# print(compute(5, 5))
# print('div -->', compute(6, 2)[3])
# #unpack the values
# a, s, m, d = compute(5, 5)
# print(a,s,m,d)
#higher order function: function than can run other functions
#string remove spaces, lowercase, remove special char
# def remove_space(text):
#     return text.strip()
# def convert_to_lowercase(text):
#     return text.lower()
# def remove_special_char(text):
#     return text.replace("?", "")
#
# text = "      Sample?TEXT         "
# print(f"X{text}X")
# text = remove_space(text)
# print(f"X{text}X")
# text = convert_to_lowercase(text)
# print(f"X{text}X")
# text = remove_special_char(text)
# print(f"X{text}X")
#
# my_pipleline = [remove_space,  convert_to_lowercase, remove_special_char]
# def clean_the_text(text, my_pipleline):
#     final_text = text
#     for func in my_pipleline:
#         final_text = func(final_text)
# #call the higher order function
# print("-" * 30)
# text = "      Sample?TEXT         "
# print(f"X{text}X")
# clean_the_text(text, my_pipleline)

# number = 88
# print(number)

# Lambda
multiplay_add = lambda n1 : n1 * 2 + 2
print(multiplay_add(2))
# Lambda 2
jahaziel = lambda j1, j2 : j1 + " Heart " + j2
print(jahaziel('Jaha', 'Clie'))
#Lambda 3
in_a_relationship = lambda value : 'Sila na' if value == 1 else 'Fake news'
import random
print(in_a_relationship(random.randint(1, 2)))

#map
numbers = [x for x in range(1, 11)]
print(numbers)

def add_one(n):
   return n + random.randint(1, 50)
final_values = list(map(add_one, numbers))
print(final_values)

#map2
numbers1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numbers2 = [13, 13, 5, 17, 35, 25, 47, 35, 48, 14]
print(numbers1, numbers2)

def add_2_numbers(n1,n2):
    return n1 + n2
map(add_2_numbers, numbers1, numbers2)
string1 = ['Alice', 'Bob', 'Charlie']
string2 = ['Angelo', 'Brespicio', 'Crespicio']
def add_two_strings(s1,s2):
    return s2 + ", " + s1
print(list(map(add_two_strings, string1, string2)))

#filters with lambda
numbers1 = [1, 20, 45, 3, 90, 6,]
final_values = list(filter(lambda x:True if x > 10 else False, numbers1))
print(final_values)
final_values = list(filter(lambda x: x % 2 == 0, numbers1))
print("Even: ", final_values)
#filter check if names start wtih A
names = ['Aaron', 'Bob', 'Andrea', 'Jim', 'AKim', 'Lim']
s = 'Aaron'
starts_with_a = list(filter(lambda s: s.startswith('A'), names))
print(starts_with_a)
a = ''
ends_with_a = list(filter(lambda s: s.endswith('m'), names))
print(ends_with_a)
#version1
as_long_as_you_have_a = [list(filter(lambda s:'a' in s, names))]
print(as_long_as_you_have_a)


