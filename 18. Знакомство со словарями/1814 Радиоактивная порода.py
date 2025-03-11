from math import gcd
from functools import reduce

halflife = {}
temp_list = input().split()
for i in range(0, len(temp_list) - 1, 2):
    halflife[temp_list[i]] = int(temp_list[i + 1])

rad_values = []
temp_list = input().split()
temp_list2 = input().split()
for i in range(len(temp_list2)):
    rad_values.append([temp_list[i], float(temp_list2[i])])

rad_ok = float(input())

step = reduce(gcd, list(halflife.values()))

days = int(step)
while 1:
    rad_current = 0.0
    for i in range(len(rad_values)):
        if days % halflife[rad_values[i][0]] == 0:
            rad_values[i][1] -= 0.5 * rad_values[i][1]
        rad_current += rad_values[i][1]
    if rad_current < rad_ok:
        break
    days += step

print(days)
print(' '.join(str(rad_values[i][1]) for i in range(len(rad_values))))
