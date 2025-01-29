cat_found = False
for i in range(int(input())):
    string = input()
    if 'Кот' in string or 'кот' in string:
        print('МЯУ')
        cat_found = True
if not cat_found:
    print('НЕТ')