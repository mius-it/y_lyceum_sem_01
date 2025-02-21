N = int(input())
datalist = []
for i in range(N):
    datalist.append(input())
searchstr = input()
for i in datalist:
    if searchstr in i:
        print(i)
