n = int(input())
pas_tri = [[1],[1,1]]
for i in range(2, n):
    tmp = []
    for j in range(i + 1):
        if j == 0 or j == i:
            tmp.append(1)
        else:
            tmp.append(pas_tri[i - 1][j - 1] + pas_tri[i - 1][j])
    pas_tri.append(tmp)
print('\n'.join([' '.join(map(str, row)) for row in pas_tri]))