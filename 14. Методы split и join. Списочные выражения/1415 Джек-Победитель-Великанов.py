n = int(input())
title = []
for i in range(n):
    templist = []
    s = input()
    while s != '*':
        templist.append(s)
        s = input()
    title.append('-'.join((' '.join(templist)).split()))

print(', '.join(title[::-1]))