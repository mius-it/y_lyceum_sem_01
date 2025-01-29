x = 0
y = 0
direction = 'север'
cmd_cntr = 0

treasure_x = int(input())
treasure_y = int(input())

while x != treasure_x or y != treasure_y:
    cmd = input()
    if cmd == 'налево':
        if direction == 'север':
            direction = 'запад'
        elif direction == 'запад':
            direction = 'юг'
        elif direction == 'юг':
            direction = 'восток'
        elif direction == 'восток':
            direction = 'север'
    elif cmd == 'направо':
        if direction == 'север':
            direction = 'восток'
        elif direction == 'восток':
            direction = 'юг'
        elif direction == 'юг':
            direction = 'запад'
        elif direction == 'запад':
            direction = 'север'
    elif cmd == 'разворот':
        if direction == 'север':
            direction = 'юг'
        elif direction == 'юг':
            direction = 'север'
        elif direction == 'запад':
            direction = 'восток'
        elif direction == 'восток':
            direction = 'запад'
    elif cmd == 'вперёд':
        steps = int(input())
        if direction == 'север':
            y += steps
        elif direction == 'юг':
            y -= steps
        elif direction == 'запад':
            x -= steps
        elif direction == 'восток':
            x += steps
    cmd_cntr += 1
print(cmd_cntr)
print(direction)