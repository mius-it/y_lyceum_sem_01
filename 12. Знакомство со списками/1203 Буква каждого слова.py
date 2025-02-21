N = int(input())
words = []
for i in range(N):
    words.append(input())
pos = int(input())
for i in words:
    if pos <= len(i):
        print(i[pos - 1], end='')