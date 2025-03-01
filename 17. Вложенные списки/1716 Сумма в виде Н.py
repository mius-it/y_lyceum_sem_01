N = int(input())
max_sumH = 0
table = []
for _ in range(N):
    table.append(list(map(int, input().split())))

for i in range(N - 2):
    for j in range(N - 2):
        sumH = 0
        sumH += (table[i][j] + table[i][j + 2] +
                 table[i + 1][j] + table[i + 1][j + 1] + table[i + 1][j + 2] +
                 table[i + 2][j] + table[i + 2][j + 2])
        if sumH > max_sumH:
            max_sumH = sumH
print(max_sumH)