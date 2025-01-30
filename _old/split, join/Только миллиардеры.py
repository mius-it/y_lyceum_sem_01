#line = input()
line = '10000,10000000000,200000;2000000000,1345678910,330000000'

magazines = line.split(';')
print("Журналы:", magazines)
for i in range(len(magazines)):
    #even_squares = [i ** 2 for i in range(10) if i % 2 == 0]
    #accounts = magazines[i].split(',')
    #billionaire = [accounts[j] for j in range(len(accounts)) if accounts[j] > 1000000000]
    #a = [int(x) for x in '976 929 289 809 7677'.split()]
    bill = [x for x in magazines[i].split(',')]
    #print("Счета:", bill)
    #for j in range(len(bill)):
    #    if int(bill[j]) > 1000000000:
    #        print(bill[j], end=", ")
    #print()
    #print([i * j for i in range(3) for j in range(3)])
    #print(bill)
    print([bill[j] for j in range(len(bill))])