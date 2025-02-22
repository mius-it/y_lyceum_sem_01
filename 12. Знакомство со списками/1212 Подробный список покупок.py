N = int(input())
purch = []
quant = []
for i in range(N):
    purch.append(input())
    quant.append(input())
for i in range(N-1, -1, -1):
    print(purch[i], quant[i])