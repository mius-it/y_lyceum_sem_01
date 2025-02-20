bulls = cows = 0
word1 = input()
word2 = input()

for i in range(len(word1)):
    for j in range(len(word1)):
        if word1[i] == word2[j]:
            if i == j:
                bulls += 1
            else:
                cows += 1
print(bulls, cows)