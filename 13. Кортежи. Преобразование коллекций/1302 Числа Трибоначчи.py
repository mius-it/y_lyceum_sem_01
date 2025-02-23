N = int(input())
while N > 75:
    N = int(input('(Введите число <= 75): '))

trib = [1, 1, 1]

for i in range(3, N):
    trib.append(trib[i - 1] + trib[i - 2] + trib[i - 3])

for num in trib:
    print(num, end=' ')