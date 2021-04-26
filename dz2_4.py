# for i, word in enumerate(text_line, 1):
#     print(i word) if len(word) <= 10 else print(i, word[:10])



text_line = input('Введи слова через пробелы - ').split()
for i, word in enumerate(text_line, 1):
    print(f'{i}) {word[:10]}')