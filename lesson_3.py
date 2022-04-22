# -*- coding: utf-8 -*-

# def f(x, my_list=None):
#     if my_list is None:
#         my_list = []
#     my_list.append(x)
#     print(my_list)
#     return sum(my_list)
# print(f(0, [1,2]))


########## Только не четные элементы возводить в квадрат ##########
########## Остаток от деления на 2 равен 0 - четные #########
########## Остаток от деления на 2 равен 1  - не четные #########
print([elem ** 2 for elem in range(10) if elem % 2 == 1])

##########
lst = list(range(10))
for element in lst:
    print(element ** 2 if element % 3 == 0 else element + 1 if element % 3 == 2 else element - 1)

##########!/usr/bin/env python3
print([elem ** 2 if elem % 2 == 1 else elem for elem in range(10)])

##########
lst = []
for first_elem in range(1, 10, 3):
    lst.append([])
    for second_elem in range(first_elem, first_elem + 3):
        lst[-1].append(second_elem)
for lst1 in lst:
    print(lst1)

##########!/usr/bin/env python3
lst = [[element for element in range(elem, elem +3)] for elem in 
range(1, 10, 3)]
print(lst)

##########!/usr/bin/env python3
d = {key: value ** 2 for key, value in enumerate(range(7))}
print(d)

import pandas as pd

ord = pd.read_excel('C:\\Users\\seligenenko\\Desktop\\tel.xlsx')
print(ord.columns)
for i in ord['Номер']:
    print (i + ' hello')