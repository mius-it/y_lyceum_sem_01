'''
|---|       |---|       |---|
|   |       |   |       |   |
| 3 |  ---  | 4 |  ---  | 5 | -КЛЧ- > ВЫХОД
|   |       |   |       |   |
|---|       |---|       |---|
  |           |           |
|---|       |---|       |---|
|   |       |   |       |   |
| 1 |  ---  | 0 |  ---  | 2 |
|КЛЧ|       |   |       |   |
|---|       |---|       |---|
'''
key_picked = False
room = 0
while 1:
    if room == 0:
        print('Вы приходите в себя в комнате №0. По крайней мере так написано на стене. '
              'Вы очень хотите найти выход отсюда. Вы осматриваетесь.')
        print('Вы можете пойти на "запад", "север" или "восток". ')
        direction = input()
        if direction == "запад":
            print("Вы идёте на запад.")
            room = 1
        elif direction == "восток":
            print("Вы идёте на восток.")
            room = 2
        elif direction == "север":
            print("Вы идёте на север.")
            room = 4
        else:
            print("Неверный ввод, повторите")
    elif room == 1:
        print('Комната №1.', end=' ')
        if key_picked:
            print('Здесь раньше лежал ключ.', end=' ')
        else:
            print('В углу поблёскивает кем-то оставленный старый ключ.', end=' ')
        print('Вы можете пойти на "север" или "восток"', end='')
        if key_picked:
            print('')
        else:
            print(', а также "подобрать ключ". ')
        direction = input()
        if direction == "север":
            print("Вы идёте на север.")
            room = 3
        elif direction == "восток":
            print("Вы идёте на восток.")
            room = 0
        elif direction == "подобрать ключ":
            if not key_picked:
                print("Вы подбираете ключ и кладёте в карман")
                key_picked = True
            else:
                print('Ключ уже в вашем кармане')
        else:
            print("Неверный ввод, повторите")
    elif room == 3:
        print('Комната №3. Ничем не примечательна. '
              'Вы можете пойти на "юг" или "восток".')
        direction = input()
        if direction == "юг":
            print("Вы идёте на юг.")
            room = 1
        elif direction == "восток":
            print("Вы идёте на восток.")
            room = 4
        else:
            print("Неверный ввод, повторите")
    elif room == 4:
        print('Комната №4. Ничем не примечательна. '
              'Вы можете пойти на "запад", "юг" или "восток".')
        direction = input()
        if direction == "юг":
            print("Вы идёте на юг.")
            room = 0
        elif direction == "восток":
            print("Вы идёте на восток.")
            room = 5
        elif direction == "запад":
            print("Вы идёте на запад.")
            room = 3
        else:
            print("Неверный ввод, повторите")
    elif room == 5:
        print('Комната №5. На восточной двери светится надпись "ВЫХОД", '
              'но, кажется, дверь заперта на ключ. '
              'Вы можете пойти на "запад", "юг" или "восток".')
        direction = input()
        if direction == "юг":
            print("Вы идёте на юг.")
            room = 2
        elif direction == "восток":
            if key_picked:
                print("Вы достаёте ключ из кармана и открываете дверь. "
                      "Вы видите свет и идёте на него. Вы чувствуете облегчение. "
                      "Вы свободны!")
                break
            else:
                print('Дверь заперта, силой не открыть. Где-то должен быть ключ... ')
        elif direction == "запад":
            print("Вы идёте на запад.")
            room = 4
        else:
            print("Неверный ввод, повторите")
    elif room == 2:
        print('Комната №2. Ничем не примечательна. '
              'Вы можете пойти на "запад", "север".')
        direction = input()
        if direction == "север":
            print("Вы идёте на север.")
            room = 5
        elif direction == "запад":
            print("Вы идёте на запад.")
            room = 0
        else:
            print("Неверный ввод, повторите")
print('Игра окончена.')