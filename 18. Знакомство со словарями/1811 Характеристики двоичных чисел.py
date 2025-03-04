nums = [bin(int(num))[2:] for num in input().split()]

numdata = []
for n in nums:
    dct = {}
    dct['digits'] = len(n)
    dct['units'] = n.count('1')
    dct['zeros'] = n.count('0')
    numdata.append(dct)

print(numdata)