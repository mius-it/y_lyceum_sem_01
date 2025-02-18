M = int(input())
food = set()
for i in range(M):
    food.add(input())

N = int(input())
for i in range(N):
    recipe = input()
    L = int(input())
    cntr = 0
    for i in range(L):
        if input() in food:
            cntr += 1
    if cntr == L:
        print(recipe)