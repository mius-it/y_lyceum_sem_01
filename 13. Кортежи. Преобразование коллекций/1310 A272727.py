N = int(input())
cntr = 0
seq = [0]
for _ in range(N - 1):
    for i in range(len(seq)):
        if seq[i] == seq[-i - 1]:
            cntr += 1
    seq.append(cntr)
    cntr = 0
for s in seq:
    print(s)