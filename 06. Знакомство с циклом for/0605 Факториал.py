n = int(input())
factorial = 1
if n > 0:
    for i in range(1, n + 1):
        factorial *= i
print(factorial)