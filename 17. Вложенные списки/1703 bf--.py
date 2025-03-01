tape = [0] * 30000
pos = 0
prg = input()

for cmd in prg:
    if cmd == '>':
        pos = (pos + 1) % 30000
    elif cmd == '<':
        pos = (pos - 1) % 30000
    elif cmd == '+':
        tape[pos] = (tape[pos] + 1) % 256
    elif cmd == '-':
        tape[pos] = (tape[pos] - 1) % 256
    elif cmd == '.':
        print(tape[pos])