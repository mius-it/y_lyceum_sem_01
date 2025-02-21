whitelist = []
searchlist = []

N = int(input())
for i in range(N):
    whitelist.append(input())

M = int(input())
for i in range(M):
    searchlist.append(input())

for request in searchlist:
    if request in whitelist:
        print(request)