import math

N = int(input())
while N >= 800:
    N = int(input())

for m in range(1, N):
    for n in range(1, m):
        x = m ** 2 - n ** 2
        y = 2 * m * n
        z = m ** 2 + n ** 2
        if math.gcd(x, y, z) > 1:
            continue
        if x > y:
            x, y = y, x
        if z <= N:
            print(x, y, z)