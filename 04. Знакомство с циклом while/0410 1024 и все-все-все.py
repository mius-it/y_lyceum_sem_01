x = int(input())
degree = 0

while x != 1:
    if x % 2 != 0:
        print('НЕТ')
        break
    x /= 2
    degree += 1
else:
    print(degree)