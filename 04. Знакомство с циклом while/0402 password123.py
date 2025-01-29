psw1 = input()
psw2 = input()

if len(psw1) < 8:
    print('Короткий!')
elif psw1 != psw2:
    print('Различаются')
else:
    print('OK')