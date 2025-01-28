limit = int(input())
pi = 0

for i in range(limit):
    pi += (-1) ** i / (2 * i + 1)
pi *= 4

print(pi)