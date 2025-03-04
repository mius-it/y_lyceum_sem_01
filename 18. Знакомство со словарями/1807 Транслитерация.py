translit = {
    'А': 'A',
    'Б': 'B',
    'В': 'V',
    'Г': 'G',
    'Д': 'D',
    'Е': 'E',
    'Ё': 'E',
    'Ж': 'Zh',
    'З': 'Z',
    'И': 'I',
    'Й': 'I',
    'К': 'K',
    'Л': 'L',
    'М': 'M',
    'Н': 'N',
    'О': 'O',
    'П': 'P',
    'Р': 'R',
    'С': 'S',
    'Т': 'T',
    'У': 'U',
    'Ф': 'F',
    'Х': 'Kh',
    'Ц': 'Th',
    'Ч': 'Ch',
    'Ш': 'Sh',
    'Щ': 'Shch',
    'Ы': 'Y',
    'Э': 'E',
    'Ю': 'Iu',
    'Я': 'Ia',
}
phrase = input()
for c in phrase:
    if c == 'ё':
        c = 'е'
    elif c == 'Ё':
        c = 'Е'
    elif c == 'й':
        c = 'и'
    elif c =='Й':
        c = 'И'
    elif c == 'ь' or c == 'Ь' or c == 'ъ' or c == 'Ъ':
        continue

    if c.upper() in translit:
        if c.isupper():
            print(translit[c.upper()], end='')
        else:
            print(translit[c.upper()].lower(), end='')
    else:
        print(c, end='')