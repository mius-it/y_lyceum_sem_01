n = int(input())
sum_iq = 0
for i in range(n):
    iq = int(input())
    sum_iq += iq
    mid_iq = sum_iq / (i + 1)
    if iq < mid_iq:
        print('<')
    elif iq > mid_iq:
        print('>')
    else:
        print('0')