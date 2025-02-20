city1 = input()
while 1:
    city2 = input()
    if city1[-1] != city2[0]:
        break
    city1 = city2
print(city2)
