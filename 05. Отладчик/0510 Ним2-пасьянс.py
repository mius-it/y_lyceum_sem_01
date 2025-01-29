heap1 = int(input())
heap2 = int(input())

while heap1 != 0 or heap2 != 0:
    choice = input()
    take = int(input())
    if choice == '1':
        heap1 -= take
    elif choice == '2':
        heap2 -= take
    print(heap1, heap2)