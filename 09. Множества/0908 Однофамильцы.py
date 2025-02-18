N = int(input())
setA = set()
setB = set()

for i in range(N):
    name = input()
    if name in setA:
        setB.add(name)
    else:
        setA.add(name)

print(N - (len(setA) - len(setB)))
