N = int(input())
nums = []
subs = set()

for _ in range(N):
    nums.append(int(input()))

for i in range(N):
    for j in range(N):
        subs.add(nums[i] - nums[j])
subs_list = list(subs)
subs_list.sort()
print('\n'.join([str(s) for s in subs_list]))