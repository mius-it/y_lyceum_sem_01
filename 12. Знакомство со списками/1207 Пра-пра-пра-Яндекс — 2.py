datalist = []
searchstr = []

N = int(input())
for i in range(N):
    datalist.append(input())

M = int(input())
for i in range(M):
    searchstr.append(input())

cntr = 0
for i in datalist:
    for j in searchstr:
        if j in i:
            cntr += 1
    if cntr == M:
        print(i)
    cntr = 0
