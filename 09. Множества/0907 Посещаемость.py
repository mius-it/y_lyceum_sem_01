M = int(input())
setA = set()
setB = set()

for i in range(M):
    N = int(input())
    for j in range(N):
        setB.add(input())
    if len(setA) == 0:
        setA = setB.copy()
    else:
        setA = setA & setB
    setB.clear()
for i in setA:
    print(i)