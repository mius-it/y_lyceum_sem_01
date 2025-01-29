heap = int(input())
while heap > 0:
    take = int(input())
    if take > 0 and take <= 3:
        heap -= take
    print(heap)