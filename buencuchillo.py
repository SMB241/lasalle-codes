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
values = [1,4,9,7]
numbers = [[x for x in range(1,11) if x not in values] for i in range(5)]
print(numbers)
values = [1,4,9,7]
numbers = [[x for x in range(10,0, -1) if x not in values] for i in range(5)]
print(numbers)
values = [1,4,9,7]
numbers = [["x" if x % 2 == 0 else x for x in range(10,0, -1) ] for i in range(5)]
print(numbers)