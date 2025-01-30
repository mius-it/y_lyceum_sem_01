M = int(input())
N = int(input())

library_set = set()

for i in range(M):
    library_set.add(input())

for i in range(N):
    book = input()
    if book in library_set:
        print("YES")
    else:
        print("NO")