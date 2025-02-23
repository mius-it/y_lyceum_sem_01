phrase = set(input())
lat = list('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz')
rus = list('АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюя')

for letter in phrase:
    if letter in lat:
        for i in range(len(lat)):
            if letter == lat[i]:
                letup = (letter, i + 1)
                print(letup)
    elif letter in rus:
        for i in range(len(rus)):
            if letter == rus[i]:
                letup = (letter, i + 1)
                print(letup)
