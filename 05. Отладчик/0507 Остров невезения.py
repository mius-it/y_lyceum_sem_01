d = int(input())
m = int(input())
y = int(input())

c = y // 100
y %= 100

m -= 2
if m <= 0:
    m = 12 - m
    y -= 1

print((d + ((13 * m - 1) // 5 ) + y + (y // 4 + c // 4 - 2 * c + 777)) % 7)