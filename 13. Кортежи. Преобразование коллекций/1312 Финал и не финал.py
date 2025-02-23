N = int(input())
tuplist = []
for _ in range(N):
    tuplist.append((input(), int(input())))

for i in range(N - 1):
    for j in range(N - 1 - i):
        if tuplist[j][1] < tuplist[j + 1][1]:
            tuplist[j], tuplist[j + 1] = tuplist[j + 1], tuplist[j]

half = int(len(tuplist) // 2) + len(tuplist) % 2

for i in range(half - 1):
    for j in range(half - 1 - i):
        if tuplist[j] > tuplist[j + 1]:
            tuplist[j], tuplist[j + 1] = tuplist[j + 1], tuplist[j]
for i in range(half, N - 1):
    for j in range(half, N - 1 - i + half):
        if tuplist[j] > tuplist[j + 1]:
            tuplist[j], tuplist[j + 1] = tuplist[j + 1], tuplist[j]

for t in tuplist:
    print(t[0])
