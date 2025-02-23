N = int(input())
pup_list = []
for i in range(N):
    pup_list.append(input())

for pup in pup_list:
    print(pup)

print()

for pup in pup_list:
    if pup[-1] == '4' or pup[-1] == '5':
        print(pup)