import random

heap1 = int(input('Сколько камней в куче 1: '))
heap2 = int(input('Сколько камней в куче 2: '))

print()
print('----------------')
print()

while 1:
    if heap1 == 0:
        ai_choice = 2
    elif heap2 == 0:
        ai_choice = 1
    else:
        ai_choice = random.randint(1,2)
    if ai_choice == 1:
        ai_take = random.randint(1, heap1)
        heap1 -= ai_take
    else:
        ai_take = random.randint(1, heap2)
        heap2 -= ai_take
    print('ИИ взял', ai_take, 'камней из кучи', ai_choice)
    print('Куча 1:', heap1, 'камней. Куча 2:', heap2, 'камней.')
    if heap1 == 0 and heap2 == 0:
        print("ИИ выиграл!")
        break
# -------------
    if heap1 == 0:
        print('Камни остались только в куче 2. Берём оттуда.')
        choice = '2'
    elif heap2 == 0:
        print('Камни остались только в куче 1. Берём оттуда.')
        choice = '1'
    else:
        choice = input('Выберите кучу: ')
    take = int(input('Сколько камней взять: '))
    if choice == '1':
        while take > heap1:
            print('Нельзя взять более', heap1, 'камней. Сколько камней взять: ', end='')
            take = int(input())
        heap1 -= take
    elif choice == '2':
        while take > heap2:
            print('Нельзя взять более', heap2, 'камней. Сколько камней взять: ', end='')
            take = int(input())
        heap2 -= take
    print('Вы взяли', take, 'камней из кучи', choice)
    print('Куча 1:', heap1, 'камней. Куча 2:', heap2, 'камней.')
    if heap1 == 0 and heap2 == 0:
        print("Вы выиграли!")
        break
    print()
    print('----------------')
    print()