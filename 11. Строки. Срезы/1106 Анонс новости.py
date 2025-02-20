maxlen = int(input())
N = int(input())

for i in range(N):
    headline = input()
    if len(headline) > maxlen:
        print(headline[:maxlen-3], '...', sep='')
    else:
        print(headline)