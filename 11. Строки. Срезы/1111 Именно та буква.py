word = input()
pos = int(input())
letter = input()

if len(letter) == 1 and pos <= len(word):
    if word[pos - 1] == letter:
        print('ДА')
    else:
        print('НЕТ')
else:
    print('ОШИБКА')