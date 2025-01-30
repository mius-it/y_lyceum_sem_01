x = 0
y = 0
cmd = ''
cmd_cntr = 0
treasure_x = int(input())
treasure_y = int(input())

while x != treasure_x or y != treasure_y:
    cmd = input()
    if cmd == 'стоп':
        break
    elif cmd == 'север':
        steps = int(input())
        y += steps
    elif cmd == 'восток':
        steps = int(input())
        x += steps
    elif cmd == 'юг':
        steps = int(input())
        y -= steps
    elif cmd == 'запад':
        steps = int(input())
        x -= steps
    cmd_cntr += 1
print(cmd_cntr)