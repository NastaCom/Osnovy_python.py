"""
Создать список и заполнить его элементами различных типов данных.
Реализовать скрипт проверки типа данных каждого элемента. Использовать функцию type() для проверки типа.
Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.
"""

my_list = [5,
           5.5,
           (1 + 3j),
           'word',
           [1, 2, 3],
           (1, 2.2, 2),
           {4, 4, 4, 5, 5},
           {1: 'first', 2: 'twice'},
           True,
           None]
for i, item in enumerate(my_list, start=1):
    print(f'{i} "{item}" - {type(item)}')
