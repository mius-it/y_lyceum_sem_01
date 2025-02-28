n = int(input())
cntr = 0
word = input()
for _ in range(n):
    string = input()
    if word in string or 'забыл' in string:
        cntr += 1
if cntr < n / 2:
    print('НЕ ТАК И МНОГО')
else:
    print('ВСЕ РАВНО НИЧЕГО СТРАШНОГО')
print(cntr)