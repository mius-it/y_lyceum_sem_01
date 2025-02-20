maxlen = 0
maxword = ''
word = input()
minlen = len(word)
minword = word

while word != 'стоп':
    wordlen = len(word)
    if wordlen > maxlen:
        maxlen = wordlen
        maxword = word
    if wordlen < minlen:
        minlen = wordlen
        minword = word
    word = input()

cntr = 0
for i in range(minlen):
    if minword[i] in maxword:
        cntr += 1

if cntr == minlen:
    print('ДА')
else:
    print('НЕТ')