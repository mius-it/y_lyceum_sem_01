for i in range(1, 10000):
    sumdiv1 = sumdiv2 = 0
    for j in range(1, i):
        if i % j == 0:
            sumdiv1 += j
    for j in range(1, sumdiv1):
        if sumdiv1 % j == 0:
            sumdiv2 += j
    if i == sumdiv2 and i < sumdiv1:
        print(i, sumdiv1)
