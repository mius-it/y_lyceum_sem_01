etc = []
string = input()
while string != '':
    etc.append(string)
    string = input()

sbad_psw = input()
bad_psw = sbad_psw.split(';')

for i in range(len(etc)):
    ls_etc = etc[i].split(':')
    for j in range(len(bad_psw)):
        if ls_etc[1] == bad_psw[j]:
            print('To:', ls_etc[0])
            print(ls_etc[4].split(',')[0], ', ваш пароль слишком простой, смените его.')
            break
            