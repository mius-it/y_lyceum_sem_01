N = int(input())
tbl = []
sumtbl = 0

for _ in range(N):
    tbl.append(input().split(', '))

for i in range(N):
    tbl[i][i], tbl[i][N - 1 - i] = tbl[i][N - i - 1], tbl[i][i]
    sumtbl += int(tbl[i][i]) + int(tbl[i][N - 1 - i])

print()
print('\n'.join([' '.join(ch) for ch in tbl]))

print(sumtbl)
