import random

heap = int(input())
while 1:
    if heap < 3:
        ai_take = random.randint(1, heap)
    else:
        ai_take = random.randint(1, 3)
    heap -= ai_take
    print(ai_take, heap)
    if heap == 0:
        print("ИИ выиграл!")
        break

    take = int(input())
    while not (take > 0 and take <= 3 and take <= heap):
        print('Некорректный ход:', take)
        take = int(input())
    heap -= take
    print(take, heap)
    if heap == 0:
        print("Вы выиграли!")
        break
