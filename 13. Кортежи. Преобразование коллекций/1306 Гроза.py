N = int(input())
places = []

for i in range(N):
    places.append((int(input()), float(input())))

for i in range(N - 1):
    for j in range(N - 1 - i):
        if places[j] < places[j + 1]:
            places[j], places[j + 1] = places[j + 1], places[j]

for p in places:
    print(p)
