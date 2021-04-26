list = [5, 5.5, (-8 + 0j), 'text', [1, 2, 3], (1 , 2, 3.5), {1, 2, 3}, {1: 'январь', 2: 'февраль'}, True, (b'text'), None]
for i, item in enumerate (list):
    print(f"i{item} - {type(item)}")