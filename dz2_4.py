"""
Пользователь вводит строку из нескольких слов, разделённых пробелами. Вывести каждое
слово с новой строки. Строки нужно пронумеровать. Если слово длинное, выводить только
первые 10 букв в слове.
"""

my_list = input('Введите строку из нескольких слов, разделенных пробелами: ').split()
for i, word in enumerate(my_list, start=1):
    print(f'{i} {word[:10]}')
