N = int(input())
list_str = []
for i in range(N):
    list_str.append(input())
for s in list_str:
    if 'xxx' in s:
        print('x')
        break
    if 'ooo' in s:
        print('o')
        break
else:
    for i in range(N):
        line = ''
        for s in list_str:
            line += s[i]
        if 'xxx' in line:
            print('x')
            break
        if 'ooo' in line:
            print('o')
            break
    else:
        print('-')