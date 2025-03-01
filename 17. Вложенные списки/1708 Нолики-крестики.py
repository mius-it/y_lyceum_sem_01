N = int(input())
list_str = []
for i in range(N):
    list_str.append(input())

for row in list_str:
    if 'xxx' in row:
        print('x')
        break
    if 'ooo' in row:
        print('o')
        break
else:
    for i in range(N):
        col = ''
        for s in list_str:
            col += s[i]
        if 'xxx' in col:
            print('x')
            break
        if 'ooo' in col:
            print('o')
            break
    else:
        print('-')