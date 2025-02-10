BULL = 20000
COW = 10000
CALF = 5000

price = int(input()) * 1000
herd = int(input())

for bulls in range (1, herd):
    for cows in range(herd):
        for calfs in range(herd):
            if ((bulls * BULL + cows * COW + calfs * CALF == price) and
                    (bulls + cows + calfs == herd)):
                print(bulls, cows, calfs)