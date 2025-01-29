psw = int(input())
part1 = psw // 100 + (psw // 10) % 10
part2 = (psw // 10) % 10 + psw % 10
if part1 > part2:
    print(part1, part2, sep='')
else:
    print(part2, part1, sep='')