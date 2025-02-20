cntr = 0
cntrmax = 0
string = input()

for i in string:
    if i == 'о':
        cntr += 1
    if i == 'р':
        cntr = 0
    if cntr > cntrmax:
        cntrmax = cntr
print(cntrmax)