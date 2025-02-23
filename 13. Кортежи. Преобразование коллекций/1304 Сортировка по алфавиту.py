N = int(input())
strings = []

for i in range(N):
    strings.append(input())

for i in range(N - 1):
    for j in range(N - 1 - i):
        if strings[j] > strings[j + 1]:
            strings[j], strings[j + 1] = strings[j + 1], strings[j]

for s in strings:
    print(s)