bill = []
sumstr = input()
N = int(sumstr[:3])
sum = int(sumstr[4:])
realsum = 0

for i in range(N):
    bill.append(input())

for entry in bill:
    realsum += int(entry[:7]) * int(entry[8:12])
print(sum - realsum)
for i in range(len(bill)):
    if int(bill[i][:7]) * int(bill[i][8:12]) != int(bill[i][13:]):
        print(i + 1, end=' ')
