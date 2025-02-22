rle = input()
cntr = 1
digit = rle[0]

for i in range(1, len(rle)):
    if rle[i] == digit:
        cntr += 1
    else:
        print(cntr, digit)
        digit = rle[i]
        cntr = 1
print(cntr, digit)