BULL = 20000
COW = 10000
CALF = 5000

price = int(input()) * 1000
herd = int(input())

for bulls in range (1, herd + 1):
    for cows in range(herd + 1):
        for calfs in range(herd + 1):
            if ((bulls * BULL + cows * COW + calfs * CALF == price) and
                    (bulls + cows + calfs == herd)):
                print(bulls, cows, calfs)