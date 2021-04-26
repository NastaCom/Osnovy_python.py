
revenue = float(input('Выручка - '))
costs = float(input('Издержки - '))
result = revenue - costs
if result > 0:
    print(f'Компания работает с прибылью {result}')
    print(f'Рентабельность выручки - {result / revenue:.3f}')
    persons = int(input('Количество сотрудников в штате -  '))
    print(f'Прибыль на одного сотрудника - {result / persons:.3f}')
elif result < 0:
    print(f'Компания работает с убытком - {-result}')
else:
    print(f'Нет прибыли и убытков')
