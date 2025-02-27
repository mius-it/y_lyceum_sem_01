s = input().lower().replace(' ', '')
cmax = (max(s.count(c) for c in s))
for c in s:
    if s.count(c) == cmax:
        print(c)
        break