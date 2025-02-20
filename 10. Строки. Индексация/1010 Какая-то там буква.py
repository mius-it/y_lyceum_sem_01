word = input()
num = int(input())

if num <= 0 or num > len(word):
    print('ОШИБКА')
else:
    print(word[num - 1])