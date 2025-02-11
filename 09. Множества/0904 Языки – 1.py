M = int(input())
N = int(input())
list_all = set()

for i in range (M + N):
    list_all.add(input())
onlyone = M + N - (M + N - len(list_all)) * 2
if onlyone:
    print(onlyone)
else:
    print('NO')