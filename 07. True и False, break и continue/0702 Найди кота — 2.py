cat_str = -1
str_num = 1
string = input()
while string != 'СТОП':
    if 'Кот' in string or 'кот' in string:
        if cat_str == -1:
            cat_str = str_num
    string = input()
    str_num += 1
print(cat_str)