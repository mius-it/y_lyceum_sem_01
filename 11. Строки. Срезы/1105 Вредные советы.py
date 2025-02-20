N = int(input())
for i in range(N):
    advice = input()
    if advice[:2] == 'не' or advice[:2] == 'Не':
        print(advice[3:])
    else:
        print(advice)