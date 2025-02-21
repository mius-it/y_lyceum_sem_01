N = int(input())
for i in range(N):
    cat = input()
    for j in range(len(cat)-2):
        if cat[j:j + 3] == 'кот':
            print(i + 1, j + 1)
            break
