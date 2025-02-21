word = input()
wlen = int(len(word) // 2)

if len(word) % 2:
    print(' ' * (wlen), word[wlen], ' ' * (wlen + 1), sep='')
    for i in range(1, wlen + 1):
        print(' ' * (wlen - i), word[wlen - i], ' ' * (i * 2 - 1), word[wlen + i], sep='')
else:
    for i in range(wlen):
        print(' ' * (wlen - i), word[wlen - i - 1], ' ' * i * 2, word[wlen + i], sep='')
