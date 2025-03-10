N = int(input())
words = []
freq = {}

for _ in range(N):
    phrase = (input().replace(',', '').replace('.', '').replace('!','').
              replace('?','').replace(':', '').replace(';', ''))
    words.extend(str(p).capitalize() for p in phrase.split())

for w in words:
    freq[w] = words.count(w)

freqlist = [(value, key) for key, value in freq.items()]

print('\n'.join(fl[1] for fl in sorted(freqlist, key=lambda x: (-x[0], x[1]))))

