candies = int(input())
min_grandfather = candies

for i in range(2, candies):
    additional_candies = 0
    for j in range(i):
        additional_candies += j

    if additional_candies > candies:
        break

    if (candies - additional_candies) % i == 0:
        x = (candies - additional_candies) / i
        if x == 0:
            break
        if x < min_grandfather:
            min_grandfather = int(x)
print(min_grandfather)