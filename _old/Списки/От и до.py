N = int(input())
numbers = []
for i in range(N):
    line = int(input())
    numbers.append(line)
p = int(input())
q = int(input())
sum_num = sum(numbers[p - 1:q])
print(sum_num)