#print(' '.join(input().split()[2::3]))
phrase = input().split()
for i in range(2, len(phrase), 3):
    print(phrase[i], end = ' ')