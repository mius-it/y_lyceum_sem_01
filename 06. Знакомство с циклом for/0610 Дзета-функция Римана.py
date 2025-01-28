pi = 3.141592653589793
sum_temp = 0
n = int(input())
if n <= 1300000:
    for i in range(1, n + 1):
        sum_temp += 1 / i ** 2
    print(pi ** 2 / sum_temp)