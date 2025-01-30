limit = int(input())
pi = 0

for i in range(limit):
    pi += 4 * (((-1) ** i) / (2 * i + 1))

print(pi)