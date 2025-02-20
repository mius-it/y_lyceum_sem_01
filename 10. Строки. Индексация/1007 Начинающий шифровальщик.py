msg = input()
for i in range(len(msg) - 1):
    print(ord(msg[i]), end=', ')
print(ord(msg[-1]))