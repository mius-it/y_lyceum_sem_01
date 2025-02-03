import math

side = float(input())
speed = float(input())

turns = 0
while side > speed:
    turns += 1
    side = round(math.sqrt((side - speed) ** 2 + speed ** 2), 2)

print(turns)
