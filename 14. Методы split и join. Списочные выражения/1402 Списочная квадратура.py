#print('\n'.join([str(x * x) for x in range(int(input()))]))

n = int(input())
lst = [x ** 2 for x in range(n)]
for l in lst:
    print(l)