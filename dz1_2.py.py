

#sec = int(input ('Введи время в секундах: '))

#hr = sec // 3600
#min = ((sec // 60)) % 60
#sec = sec % 60
time = int(input ('Введи время в секундах: '))
sec = time % 60
time = time - sec
hr = time // 3600
time = time - (hr * 3600)
min = time // 60
print(f'{hr}:{min}:{sec}')