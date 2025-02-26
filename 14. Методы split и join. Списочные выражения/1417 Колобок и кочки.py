n = int(input())
jumps = []
phrases = []
word = ''

for _ in range(n):
    jumps.append(int(input()))
for _ in range(n):
    phrases.append(input())

for i in range(n):
    for j in range(len(phrases[i])):
        cntr = 0
        for k in range(j, len(phrases[i])):
            if phrases[i][j] == phrases[i][k]:
                cntr += 1
        if cntr == jumps[i]:
            word += phrases[i][j]
            break
print(word)
