num = int(input())

d1 = num // 1000
d2 = (num % 1000) // 100
d3 = (num % 100) // 10
d4 = num % 10

if d1 > d2:
    d1, d2 = d2, d1
if d1 > d3:
    d1, d3 = d3, d1
if d1 > d4:
    d1, d4 = d4, d1
if d2 > d3:
    d2, d3 = d3, d2
if d2 > d4:
    d2, d4 = d4, d2
if d3 > d4:
    d3, d4 = d4, d3

print(str(d1) + str(d2) + str(d3) + str(d4))