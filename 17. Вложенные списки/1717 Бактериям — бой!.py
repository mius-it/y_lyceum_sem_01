n = int(input())
table = [[0] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        table[i][j] = int(input())

k = int(input())
for _ in range(k):
    y, x = int(input()), int(input())
    table[x][y] -= 4
    for i in range(x - 1, x + 2):
        for j in range(y - 1, y + 2):
            if i < 0 or j < 0:
                continue
            table[i][j] -= 4
            if table[i][j] < 0:
                table[i][j] = 0

print('\n'.join(' '.join(map(str, row)) for row in table))