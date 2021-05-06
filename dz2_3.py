"""
Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить, к какому времени года
относится месяц (зима, весна, лето, осень). Напишите решения через list и dict.
"""

# Решение через list

# season = ['зима', 'весна', 'лето', 'осень']
# month = int(input('Введите месяц в виде целого числа от 1 до 12 - '))
# print(season[month // 3 % 4])

# Решение через dict

month = int(input('Ведите месяц в виде числа от 1 до 12 - '))
winter = {'зима': [1, 2 , 12]}
spring = {'весна': [3, 4, 5]}
summer = {'лето': [6, 7, 8]}
autumn = {'осень': [9, 10, 11]}
if month == 1 or month == 2 or month == 12:
    print(winter.keys())
elif month == 3 or month == 4 or month == 5:
    print(spring.keys())
elif month == 6 or month == 7 or month == 8:
    print(summer.keys())
elif month == 9 or month == 10 or month == 11:
    print(autumn.keys())