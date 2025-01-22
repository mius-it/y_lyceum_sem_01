num = int(input())

dig1 = num // 100
dig2 = (num // 10) % 10
dig3 = num % 10

max = dig1
if dig2 > max:
    max = dig2
if dig3 > max:
    max = dig3

min = dig1
if dig2 < min:
    min = dig2
if dig3 < min:
    min = dig3

if (dig1 == max or dig1 == min) and (dig2 == max or dig2 == min):
    last = dig3
elif (dig1 == max or dig1 == min) and (dig3 == max or dig3 == min):
    last = dig2
else:
    last = dig1

if (min + max) / 2 == last:
    print('Вы ввели красивое число')
else:
    print('Жаль, вы ввели обычное число')