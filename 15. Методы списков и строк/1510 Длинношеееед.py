string = input().lower()
mx = 0

for ch in string:
    cntr = string.count(ch)
    if cntr > mx:
        mx = cntr

print(mx)
