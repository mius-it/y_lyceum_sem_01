string = input()
stack = []

for char in string.split():
    if char.isdigit():
        stack.append(int(char))
    else:
        if char == '+':
            stack.append(stack.pop() + stack.pop())
        elif char == '-':
            stack.append(stack.pop(-2) - stack.pop(-1))
        elif char == '*':
            stack.append(stack.pop() * stack.pop())
        elif char == '/':
            stack.append(stack.pop(-2) // stack.pop(-1))
        elif char == '~':
            stack.append((-1) * stack.pop())
        elif char == '!':
            fact = 1
            for i in range(1, stack.pop() + 1):
                fact *= i
            stack.append(fact)
        elif char == '#':
            stack.append(stack[-1])
        elif char == '@':
            c, b, a = stack.pop(), stack.pop(), stack.pop()
            stack.append(b)
            stack.append(c)
            stack.append(a)
print(stack[0])