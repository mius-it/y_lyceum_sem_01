size = int(input())
if size <= 9:
    for i in range(size, 0, -1):
        for j in range(size):
            print(chr(ord('A') + j), i, sep='', end=' ')
        print()