print("Сколько в 1 куче? ", end="") # end="" - это, чтобы не было переноса строки
heap1 = int(input())
print("Сколько вo 2 куче? ", end="")
heap2 = int(input())

while heap1 > 0 or heap2 > 0:
    print("Из какой кучи брать? ", end="")
    my_choice = int(input())
    print("Сколько камней забрать? ", end="")
    sub = int(input())
    if my_choice == 1:
        heap1 -= sub
    elif my_choice == 2:
        heap2 -= sub
    print(heap1, heap2)