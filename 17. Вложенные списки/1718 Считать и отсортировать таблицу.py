rows = int(input())
cols = int(input())
table = [[''] * cols for _ in range(rows)]

for r in range(rows):
    for c in range(cols):
        table[r][c] = input()

for row in table:
    if row is not table[0] and row is not table[-1]:
        row.sort()
    print('\t'.join(row))