N = int(input())
bd = {}
for _ in range(N):
    item = input().split()
    if item[2] not in bd:
        bd[item[2]] = list()
    bd[item[2]].append(item[0])

M = int(input())
for _ in range(M):
    print(' '.join(sorted(bd.get(input(), ''))))
