h = int(input())
w = int(input())
symb = input()

for i in range(h):
    for j in range(w):
        if i == 0 or i == h - 1 or j == 0 or j == w - 1:
            print(symb, end="")
        else:
            print(" ", end="")
    print()