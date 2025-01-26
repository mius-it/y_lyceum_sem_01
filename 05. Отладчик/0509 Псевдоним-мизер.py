import random

heap = int(input())
while 1:
    if heap == 1 or heap == 2 or heap == 6:
        ai_take = 1
    elif heap == 3 or heap == 7:
        ai_take = 2
    elif heap == 4 or heap == 8:
        ai_take = 3
    else:
        ai_take = random.randint(1, 3)
    heap -= ai_take
    print(ai_take, heap)
    if heap == 0:
        print("ИИ проиграл!")
        break

    take = int(input())
    while not (take > 0 and take <= 3 and take <= heap):
        print('Некорректный ход:', take)
        take = int(input())
    heap -= take
    print(take, heap)
    if heap == 0:
        print("Вы проиграли!")
        break
