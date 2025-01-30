num = int(input())
while num:
    if num % 3 == 0 and num % 7 == 0:
        print('Караул!')
        break
    elif num % 3 == 0:
        print('несчастливое')
    elif num % 7 == 0:
        print('опасное')
    else:
        print(num)
    num = int(input())