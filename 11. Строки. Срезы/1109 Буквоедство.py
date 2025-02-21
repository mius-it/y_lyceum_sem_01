s = input()
print(s)
for i in range(1, int(len(s) / 2 + 1)):
    print(s[i:-i])