tape = [0] * 30000
position = 0
#program = ">>++[-[-].]"
program = "+++++++++++++++++++++++++++>+++++++++++++++++++++++>+++>+++++++++++++++++++++++++++++++++++++++++++++++>--->------------>++++++++++++++++++++++++++++++++++++++++++++++++++++>+.[<[-<]>[>]>[<-[>]<.>>]<<+]"
#program = "++>+++++>+++>++++++>-->--->++>+[<[-<]>[>]>[<-[>]<.>>]<<+]"

i = 0
br_cntr = 0

def makeview (tape, program):                       # ---------------------------------
    if position == 0:
        view_tape = tape
    else:
        view_tape = []
        view_tape.append(tape[:position])
        view_tape.append(tape[position])
        view_tape.append(tape[position+1:])
    if i == 0:
        view_prog = program
    else:
        view_prog = program[:i] + "|" + program[i] + "|" + program[i+1:]
    return view_tape, view_prog

while i < len(program):
    view_tape, view_prog = makeview(tape, program)      # ---------------------------------

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
        view_tape, view_prog = makeview(tape, program)      # ---------------------------------
    elif '<' in program[i]:
        position -= 1
        if position == -1:
            position = 29999
        view_tape, view_prog = makeview(tape, program)  # ---------------------------------
    elif '.' in program[i]:
        print(tape[position])
    elif '[' in program[i]:
        br_cntr = 1
        if tape[position] == 0:
            while ']' not in program[i] or br_cntr > 0:
                i += 1
                view_tape, view_prog = makeview(tape, program)  # ---------------------------------
                if '[' in program[i]:
                    br_cntr += 1
                elif ']' in program[i]:
                    if br_cntr > 0:
                        br_cntr -= 1
    elif ']' in program[i]:
        br_cntr = 1
        while '[' not in program[i] or br_cntr > 0:
            i -= 1
            view_tape, view_prog = makeview(tape, program)  # ---------------------------------
            if ']' in program[i]:
                br_cntr += 1
            elif '[' in program[i]:
                if br_cntr > 0:
                    br_cntr -= 1
        continue
    i += 1