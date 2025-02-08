N = int(input())
cntr = 0
cntr_max = 1
for i in range(1, N + 1):
    print(i, end=' ')
    cntr += 1
    if cntr == cntr_max:
        print()
        cntr_max += 1
        cntr = 0