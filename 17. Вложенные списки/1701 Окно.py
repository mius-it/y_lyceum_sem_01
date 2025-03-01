n = int(input())
milk = []

for _ in range(n):
    milk.append(int(input()))

minmilk = int(input())
maxmilk = int(input())

for bottle in milk:
    if minmilk <= bottle <= maxmilk:
        print(bottle)