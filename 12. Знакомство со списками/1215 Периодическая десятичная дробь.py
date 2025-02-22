n = int(input())
fract = 1 / n
print('fract = ', fract)
flist = list(str(fract))
period = []
print('len = ', len(flist))

if len(flist) >= 18:
    for i in range(2, len(flist) - 1):
        for j in range(i + 1, len(flist)):
            if flist[i] == flist[j]:
                period = flist[i: j]
                break
        if period:
            break
else:
    print('0')

for c in period:
    print(c, end='')
