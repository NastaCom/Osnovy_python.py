list = input('Заполните с использованием пробелов список любыми символами: ').split()
for i in range(1, len(list), 2):
    list.insert(i - 1, list.pop(i))
print('Мы реализовали обмен значений соседних элементов: ', list)



#for el in range(1, len(list.index(el)), 2):
#    (list[el - 1], list[el] = list[el], list[el - 1]).pos(el)
# print(list)

#i = 0
#print(f'{list}')
#while i + 1 < len(list):
#    if i % 2 == 0:
#        list.insert(i, list.pop(i + 1))
#    i += 1
#for i in list(0, list[i]):
#for el in range(len(list)):
#    if list[el] == sign:
#        list.insert(el +1, sign)
#        break
#    elif list[0] < sign:
#        list.insert(0, sign)
#for i in reversed(list):

