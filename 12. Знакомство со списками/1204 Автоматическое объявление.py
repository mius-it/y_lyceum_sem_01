N = int(input())
words = []
for i in range(N):
    words.append(input())
parts = int(input())
for i in range(parts):
    part = int(input()) - 1
    print(words[part])