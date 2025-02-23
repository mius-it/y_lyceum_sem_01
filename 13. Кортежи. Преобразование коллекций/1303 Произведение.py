N = int(input())
nums = []
is_mul = False

for i in range(N):
    nums.append(int(input()))
mul = int(input())

for i in range(len(nums)):
    for j in range(len(nums)):
        if mul == nums[i] * nums[j] and i != j:
            is_mul = True
            break
    if is_mul:
        print('ДА')
        break
else:
    print('НЕТ')