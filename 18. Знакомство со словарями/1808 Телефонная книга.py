N = int(input())
phonebook = {}
for _ in range(N):
    item = input().split()
    if item[1] not in phonebook:
        phonebook[item[1]] = list()
    phonebook[item[1]].append(item[0])

M = int(input())
for _ in range(M):
    name = input()
    if name in phonebook:
        print(' '.join(phonebook[name]))
    else:
        print('Нет в телефонной книге')
