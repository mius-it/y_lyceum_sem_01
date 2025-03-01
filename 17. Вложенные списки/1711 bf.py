tape = [0] * 30000
pos = 0
prg = input()
i = 0
bracket_counter = 0

while i < len(prg):
    if prg[i] == '>':
        pos = (pos + 1) % 30000
    elif prg[i] == '<':
        pos = (pos - 1) % 30000
    elif prg[i] == '+':
        tape[pos] = (tape[pos] + 1) % 256
    elif prg[i] == '-':
        tape[pos] = (tape[pos] - 1) % 256
    elif prg[i] == '.':
        print(tape[pos])
    elif prg[i] == '[':
        bracket_counter = 1
        if tape[pos] == 0:
            while prg[i] != ']' or bracket_counter > 0:
                i += 1
                if prg[i] == '[':
                    bracket_counter += 1
                elif prg[i] == ']':
                    if bracket_counter > 0:
                        bracket_counter -= 1
    elif prg[i] == ']':
        bracket_counter = 1
        while prg[i] != '[' or bracket_counter > 0:
            i -= 1
            if prg[i] == ']':
                bracket_counter += 1
            elif prg[i] != '[':
                if bracket_counter > 0:
                    bracket_counter -= 1
        continue
    i += 1