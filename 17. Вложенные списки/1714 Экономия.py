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

A, B = (int(x) for x in input().split())

minprice = table[A][B]
beststation = A
for i in range(N):
    guess = table[A][i] + table[i][B]
    if (i != A and i != B) and (guess < minprice):
        minprice = guess
        beststation = i

print(beststation)