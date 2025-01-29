for i in range(int(input())):
    string = input()
    if 'Кот' in string or 'кот' in string:
        print('МЯУ')
        break
else:
    print('НЕТ')