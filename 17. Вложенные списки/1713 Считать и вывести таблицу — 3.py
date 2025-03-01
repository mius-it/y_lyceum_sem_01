rows = int(input())
cols = int(input())
tbl = [[''] * cols for _ in range(rows)]

for r in range(rows):
    for c in range(cols):
        tbl[r][c] = input()

print('\n'.join(['\t'.join(ch) for ch in tbl]))