x = float(input())

if abs(x) < 0.000001 or x == 0:
    print(1000000)
else:
    print(1 / x)