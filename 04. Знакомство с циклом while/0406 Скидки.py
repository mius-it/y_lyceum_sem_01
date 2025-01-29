price = float(input())
sum = 0
while price > 0:
    if price > 1000:
        price *= 1.05
    sum += price
    price = float(input())
print(sum)