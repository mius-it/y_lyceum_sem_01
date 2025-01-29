psw1 = input()
psw2 = input()

while 1:
    if len(psw1) < 8:
        print('Короткий!')
    elif "123" in psw1:
        print('Простой!')
    elif psw1 != psw2:
        print('Различаются.')
    else:
        print('OK')
        break
    psw1 = input()
    psw2 = input()