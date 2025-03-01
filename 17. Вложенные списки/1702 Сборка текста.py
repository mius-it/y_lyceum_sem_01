order = [int(s) for s in input().split()]
string = input().split()

for i in range(len(order)):
    if i == 0:
        print(string[order[i] - 1].capitalize(), end = ' ')
    else:
        print(string[order[i] - 1].lower(), end = ' ')