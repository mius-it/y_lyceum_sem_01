rows = int(input())
cols = int(input())
tbl = [[''] * cols for _ in range(rows)]

for r in range(rows):
    for c in range(cols):
        tbl[r][c] = input()

for r in range(rows):
    for c in range(cols):
        print(tbl[r][c], end='\t')
    print()
print()
for r in range(cols):
    for c in range(rows):
        print(tbl[c][r], end='\t')
    print()