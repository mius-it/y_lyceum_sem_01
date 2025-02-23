n0 = int(input())
thimble = []
thimble2 = []
for _ in range(n0):
    thimble.append(input())

k = int(input())
for _ in range(k):
    thimbles_count = int(input())
    for i in range(thimbles_count):
        thimble2.append(thimble[int(input()) - 1])
    thimble.clear()
    thimble = thimble2.copy()
    thimble2.clear()

for t in thimble:
    print(t)