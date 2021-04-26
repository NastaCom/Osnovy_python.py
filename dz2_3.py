month = int(input('Введи месяц в числовом формате от 1 до 12: '))
sezon_vesna_dict = {
     'весна':[3, 4, 5]}
sezon_leto_dict = {
     'лето': [6, 7, 8]}
sezon_osen_dict = {
     'осень': [9, 10, 11]}
sezon_zima_dict = {
     'зима': [12, 1, 2]}

if month in sezon_vesna_dict and month >= 3 or month <= 5:
    print('время года введенного месяца - ', sezon_vesna_dict.keys())
elif month in sezon_leto_dict and month >= 6 or month <= 8:
    print('время года введенного месяца - ', sezon_leto_dict.keys())
elif month in sezon_osen_dict and month >= 9 or month <= 11:
    print('время года введенного месяца - ', sezon_osen_dict.keys())
elif month in sezon_zima_dict and (month == 12 and month <= 2 or month >= 1):
    print('время года введенного месяца - ', sezon_zima_dict.keys())
else:
    print('Такого месяца нет. Введи от 1 до 12')


