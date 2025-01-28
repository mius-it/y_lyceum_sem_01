heap = int(input())
min_x = heap
for i in range(1, heap):
    tempsum = 0
    for j in range(i):
        tempsum += j
    if tempsum > heap:
        break
    x = (heap - tempsum) / i
    if x > 0 and x < min_x and x % 1 == 0:
        min_x = int(x)
print(min_x)