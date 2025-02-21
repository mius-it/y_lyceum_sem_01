path = input()
x = 0
sline = path[0]

for move in path[1:]:
    if move == '>':
        x += 1
        sline += path[0]
    elif move == '<':
        x -= 1
        sline = sline[:x] + path[0] + sline[x + 1:]
    elif move == 'V':
        print(sline)
        sline = ' ' * x + path[0]
print(sline)
