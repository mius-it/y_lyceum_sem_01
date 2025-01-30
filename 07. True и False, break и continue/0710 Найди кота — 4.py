cat_found = False
for i in range(int(input())):
    string = input()
    if 'Кот' in string or 'кот' in string:
        cat_found = True
    elif 'Пёс' in string or 'пёс' in string:
        cat_found = False
if cat_found:
    print('МЯУ')
else:
    print('НЕТ')