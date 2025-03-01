N = int(input())
src = []
table = [[''] * N for i in range(N)]

for _ in range(N - 1):
    src.append(input().split())

for i in range(N):
    for j in range(N):
        if i == j:
            table[i][j] = 0
        elif j > i:
            table[i][j] = int(src[j - 1][i])
        else:
            table[i][j] = int(src[i - 1][j])

for A in range(N):
    for B in range(A + 1, N):
        minprice = table[A][B]
        for i in range(N):
            guess = table[A][i] + table[i][B]
            if guess < minprice:
                print(A, B)
                break