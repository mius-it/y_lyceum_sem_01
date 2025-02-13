M = int(input())
N = int(input())
K = int(input())
list_123 = set()
list_23 = set()
list_3 = set()

for i in range (M + N + K):
    pupil = input()
    if pupil not in list_123:
        list_123.add(pupil)
    elif pupil not in list_23:
        list_23.add(pupil)
    else:
        list_3.add(pupil)
exactly_2 = len(list_23) - len(list_3)
if exactly_2:
    print(exactly_2)
else:
    print('NO')
