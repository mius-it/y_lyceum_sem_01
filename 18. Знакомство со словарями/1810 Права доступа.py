N = int(input())
permissions = []
for _ in range(N):
    permissions.append(input())

M = int(input())
for _ in range(M):
    path = input()
    if '.' in path:
        path = path[:path.rfind('/')]
    print(path)
    for p in permissions:
        if path in p and p.find(path) == 0:
            print('YES')
            break
    else:
        print('NO')