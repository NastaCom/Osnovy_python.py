
while True:
    day = 1
    f_day = float(input('Результат пробежки первого дня в км: '))
    n_day = float(input('Необходимый результат: '))
    if f_day <= 0 or n_day < 0:
        print('!= 0')

    else:
        while f_day < n_day:
            f_day *=1.1
            day += 1
    print('Результат будет достигнут за', day, 'дней')
