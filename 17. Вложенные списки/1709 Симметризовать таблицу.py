N = int(input())
src = []
table = [[''] * N for i in range(N)]

for _ in range(N - 1):
    src.append(input().split())

for i in range(N):
    for j in range(N):
        if i == j:
            table[i][j] = '0'
        elif j > i:
            table[i][j] = src[j - 1][i]
        else:
            table[i][j] = src[i - 1][j]

print('\n'.join([' '.join(ch) for ch in table]))