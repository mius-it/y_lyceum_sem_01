N = int(input())
nums = []
for i in range(N):
    nums.append(int(input()))
for i in range(N - 1):
    print(nums[i] + nums[i + 1])