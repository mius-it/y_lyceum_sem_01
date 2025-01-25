sum_temp = 0
day_cntr = 0
temp = float(input())
while temp > -300:
    sum_temp += temp
    day_cntr += 1
    temp = float(input())
print(sum_temp / day_cntr)