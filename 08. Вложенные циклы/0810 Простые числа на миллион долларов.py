num = int(input())

for i in range(2, num + 1):
    divider = False
    for j in range(2, i):
        if not (i % j):
            divider = True
    if not divider:
        print(i)