num = int(input())
cntr = 0
for i in range(1, num + 1):
    if num % i == 0:
        cntr += 1
        print(i, end=' ')
if cntr == 2:
    print('\nПРОСТОЕ')
else:
    print('\nНЕТ')