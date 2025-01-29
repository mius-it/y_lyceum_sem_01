print('Вы находитесь в пещере на развилке. '
      'Вы можете пойти "налево", "направо" или "прямо". '
      'Введите одно из слов в кавычках для выбора. Кавычки не вводите.')
direction = input()
while 1:
    if direction == "налево":
        print("Вы идёте налево.")
        break
    elif direction == "направо":
        print("Вы идёте направо.")
        break
    elif direction == "прямо":
        print("Вы идёте прямо.")
        break
    else:
        print("Неверный ввод, повторите")
        direction = input()