nums = [int(n) for n in input().split()]
M, K = [int(n) for n in input().split()]

print(sum(nums[M:K + 1]))
