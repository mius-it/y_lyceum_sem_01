n = int(input())
result = 0
degree = 0

for i in range(1, n + 1):
    for j in range(1, i + 1):
        if i % 2 == j % 2:
            degree += j
    result += i ** degree
    degree = 0
print(result)