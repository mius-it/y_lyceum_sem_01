op = ''
while op != 'x':
    num1 = int(input())
    op = input()
    if op == '+':
        num2 = int(input())
        res = num1 + num2
    elif op == '-':
        num2 = int(input())
        res = num1 - num2
    elif op == '*':
        num2 = int(input())
        res = num1 * num2
    elif op == '/':
        num2 = int(input())
        if num2 == 0:
            continue
        res = int(num1 / num2)
    elif op == '%':
        num2 = int(input())
        res = num1 % num2
    elif op == '!':
        if num1 <= 0:
            continue
        res = 1
        for i in range(num1):
            res *= (i+1)
    else:
        res = num1
    print(res)