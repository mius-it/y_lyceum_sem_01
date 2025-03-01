csv = []
R = int(input())
for _ in range(R):
    csv.append(input().split(','))
print(csv)

N = int(input())
for _ in range(N):
    x, y = input().split(',')
    print(csv[int(x)][int(y)])