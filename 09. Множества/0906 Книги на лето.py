M = int(input())
N = int(input())
library = set()

for i in range(M):
    library.add(input())

for i in range(N):
    if input() in library:
        print("YES")
    else:
        print("NO")