M = int(input())
N = int(input())
list_en = set()
list_de = set()

for i in range(M):
    list_en.add(input())
for i in range(N):
    list_de.add(input())

list_onlyone = list_en ^ list_de
if list_onlyone:
    print(len(list_onlyone))
else:
    print('NO')