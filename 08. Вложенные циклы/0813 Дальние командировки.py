N = int(input())
M = 0
for i in range(1, N):
    M += 1
    if i // 10 > 0:
        M += 1
    if i // 100 > 0:
        M += 1
    if M == N:
        print(i)
        break