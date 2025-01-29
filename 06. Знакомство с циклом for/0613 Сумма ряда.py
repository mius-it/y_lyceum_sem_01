n = int(input())
sum = 0
for i in range(n):
    sum += (-1) ** i * int(input())
print(sum)