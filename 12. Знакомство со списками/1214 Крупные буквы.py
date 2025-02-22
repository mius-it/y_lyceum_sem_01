psA = [' * ',
       '* *',
       '***',
       '* *',
       '* *']
psB = ['** ',
       '* *',
       '** ',
       '* *',
       '** ']
psC = [' * ',
       '* *',
       '*  ',
       '* *',
       ' * ']
string = input()
pic = [''] * 5

for s in string:
    if s == 'A':
        for i in range(5):
            pic[i] += psA[i] + '  '
    elif s == 'B':
        for i in range(5):
            pic[i] += psB[i] + '  '
    elif s == 'C':
        for i in range(5):
            pic[i] += psC[i] + '  '

for s in pic:
    print(s)