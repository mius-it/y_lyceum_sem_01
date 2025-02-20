login = input()
for letter in login:
    if not ('a' <= letter <= 'z' or '0' <= letter <= '9' or letter == '_'):
        print('Неверный символ:', letter)
        break
else:
    print('OK')
