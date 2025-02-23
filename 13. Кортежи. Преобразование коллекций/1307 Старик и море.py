N = int(input())
waves = []

for i in range(N):
    wave = input()
    waves.append((int(wave[-1]), i + 1, wave[:-2]))

for i in range(1, N):
    if waves[i][0] > waves[i - 1][0]:
        print((waves[i - 1][1], waves[i - 1][2]))