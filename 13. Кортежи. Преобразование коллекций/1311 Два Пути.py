skills = [[], []]

S = int(input())
for _ in range(S):
    skill = int(input())
    skills[0].append(skill)
    skills[1].append(skill)

N = int(input())
for _ in range(N):
    skills[int(input()) - 1][int(input())] += int(input())

for i in skills[0]:
    print(i, end=' ')
print()
for i in skills[1]:
    print(i, end=' ')
print()

cntr = 0
for i in range(len(skills[0])):
    if(skills[0][i] == skills[1][i]):
        cntr += 1
print(cntr)