"""
Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение.
При вызове функции должен создаваться объект-генератор. Функция вызывается следующим образом: for el in fact(n).
Она отвечает за получение факториала числа. В цикле нужно выводить только первые n чисел, начиная с 1! и до n!.
Подсказка: факториал числа n — произведение чисел от 1 до n. Например, факториал четырёх 4! = 1 * 2 * 3 * 4 = 24.
"""


from itertools import count


def fact(number):
    num = 1
    if number == 0:
        yield f'{number}!=1'
    for i in range(1, number + 1):
        num *= i
        yield f'{i}!={num}'
for el in fact(int(input('Факториал числа: '))):
    print(el)
