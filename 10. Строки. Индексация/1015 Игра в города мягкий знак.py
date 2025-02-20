city1 = input()
city2 = input()

if city1[-1] == city2[0] or city1[-1] == 'ь' and city1[-2] == city2[0]:
    print('ВЕРНО')
else:
    print('НЕВЕРНО')