city_july = input()
city_august = input()

if (city_july == 'Тула' and city_august != 'Пенза' and city_august != 'Тула' or
    city_august == 'Пенза' and city_july != 'Тула' and city_july != 'Пенза'):
    print('ДА')
else:
    print('НЕТ')