heap = 1
cntr = 0
n = int(input())
while n > 1:
    cntr += 1 + n % 2
    n //= 2
print(cntr)