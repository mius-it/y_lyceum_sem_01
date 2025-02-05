num1 = int(input())
num2 = int(input())
step = int(input())

for i in range(num1, num2+1, step):
    for j in range(num1, num2+1, step):
        print(i, '+', j, '=', i + j, end='\t')
    print()