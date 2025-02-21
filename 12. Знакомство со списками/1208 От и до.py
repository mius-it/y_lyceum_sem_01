N = int(input())
nums = []
for i in range(N):
    nums.append(int(input()))
p = int(input()) - 1
q = int(input())
sum = 0
for i in range(p, q):
    sum += nums[i]
print(sum)