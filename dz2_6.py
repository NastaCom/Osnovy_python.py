tovary = [
    (1, {'название': 'компьютер', 'цена': 20000, 'количество': 5, 'ед': 'шт.'}),
    (2, {'название': 'принтер', 'цена': 6000, 'количество': 2, 'ед': 'шт.'}),
    (3, {'название': 'сканер', 'цена': 2000, 'количество': 7, 'ед': 'шт.'}),
]
characteristics = {'название': '', 'цена': '', 'количество': '', 'единица измерения': ''}
analytics = {'название': [], 'цена': [], 'количество': [], 'единица измерения': []}
#f = {value}
#prod = input('Ведите f - ')
#print (characteristics)
for f in characteristics.keys():
    prod = input(f'Введите {f} - ')
    characteristics[f] = int(prod) \
    if (f == 'цена' or f == 'количество' ) \

else prod
    analytics[f].append(characteristics[f])
#tovary.append(characteristics)

for f in tovary:
    print(f'Структура товаров {tovary}:')

print(f'Аналитика о товарах:')
for key, value in analytics.items():
    print(f'{key, value}')
