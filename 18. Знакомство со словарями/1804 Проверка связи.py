dct = {}
for word in input().split():
    dct[word] = dct.get(word, 0) + 1
    print(dct[word], end=' ')