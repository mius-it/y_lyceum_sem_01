num = input()
rank = 1
result = 0
for digit in num:
    result += int(digit) * rank
    rank *= 10
print(result)