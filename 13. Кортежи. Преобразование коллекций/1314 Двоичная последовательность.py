num = int(input())
pos = int(input())

bin_num = ""
while num > 0:
    rem = num % 2
    bin_num = str(rem) + bin_num
    num = num // 2

for i in range(pos - 1):
    cntr = 0
    tmp = ''
    for j in bin_num:
        if j == '1':
            cntr += 1
    while cntr > 0:
        rem = cntr % 2
        tmp = str(rem) + tmp
        cntr = cntr // 2
    bin_num += tmp

num = 0
deg = 1
for i in range(len(bin_num) - 1, -1, -1):
    num += int(bin_num[i]) * deg
    deg *= 2
print(num)