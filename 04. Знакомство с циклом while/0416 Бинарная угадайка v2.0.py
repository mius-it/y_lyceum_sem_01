mi = 1
ma = 1001
print((ma + mi) // 2)
ans = input()
while 1:
    if ans == '>':
        mi = (ma + mi) // 2
    elif ans == '<':
        ma = (ma + mi) // 2
    elif ans == '=':
        break
    print((ma + mi) // 2)
    ans = input()