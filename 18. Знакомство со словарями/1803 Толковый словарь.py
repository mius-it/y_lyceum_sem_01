N = int(input())
dct = {}
for _ in range(N):
    item = input()
    pos = item.find(' ')
    dct[item[:pos]] = item[pos + 1:]

M = int(input())
for _ in range(M):
    print(dct.get(input(), 'Нет в словаре'))
