N = int(input())
prev_h = 0
for i in range(N):
    b = int(input())
    m = b // (256 ** 2)
    r = (b // 256) % 256
    h = b % 256
    if h > 100:
        print(i)
        break
    h_exp = (37 * (m + r + prev_h)) % 256
    if h != h_exp:
        print(i)
        break
    prev_h = h
else:
    print('-1')