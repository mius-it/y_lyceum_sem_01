N = int(input())
coords = []
for _ in range(N):
    coords.append(tuple(map(int,input().split())))
print()
print(coords)

maxpoints = 0
for i in range(N):
    cntr = 0
    for j in range(i + 1, N):
        if (coords[i][0] // 10 == coords[j][0] // 10 and
                coords[i][1] // 10 == coords[j][1] // 10):
            cntr += 1
    if cntr > maxpoints:
        maxpoints = cntr

print(maxpoints + 1)