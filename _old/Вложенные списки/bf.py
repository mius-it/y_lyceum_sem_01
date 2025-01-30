tape = [0] * 30000
position = 0
program = input()

i = 0
br_cntr = 0

while i < len(program):
    if '+' in program[i]:
        tape[position] += 1
        if tape[position] == 256:
            tape[position] = 0
    elif '-' in program[i]:
        tape[position] -= 1
        if tape[position] == -1:
            tape[position] = 255
    elif '>' in program[i]:
        position += 1
        if position == 30000:
            position = 0
    elif '<' in program[i]:
        position -= 1
        if position == -1:
            position = 29999
    elif '.' in program[i]:
        print(tape[position])
    elif '[' in program[i]:
        br_cntr = 1
        if tape[position] == 0:
            while ']' not in program[i] or br_cntr > 0:
                i += 1
                if '[' in program[i]:
                    br_cntr += 1
                elif ']' in program[i]:
                    if br_cntr > 0:
                        br_cntr -= 1
    elif ']' in program[i]:
        br_cntr = 1
        while '[' not in program[i] or br_cntr > 0:
            i -= 1
            if ']' in program[i]:
                br_cntr += 1
            elif '[' in program[i]:
                if br_cntr > 0:
                    br_cntr -= 1
        continue
    i += 1