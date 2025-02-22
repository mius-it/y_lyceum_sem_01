N = int(input())
M = int(input())
pic = []

for i in range(N):
    pic.append(list(input()))

for i in range(N):
    if i % 2 == 0:
        for j in range(M):
            if j % 2 == 0:
                print(pic[i][j], end='')
        print()