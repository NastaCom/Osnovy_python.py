
numbers = int(input('Введи целое положительное число и я покажу в нем самую большую цифру: '))
numb = numbers%10
while numbers > 0:
    if numbers%10 > numb:
        numb = numbers%10
    numbers = numbers//10
print ('Самая большая цифра в твоем числе: ', numb)
