string = input()
nums = []

for char in string.split():
    if char.isdigit():
        nums.append(int(char))
    else:
        if char == '+':
            nums.append(nums.pop() + nums.pop())
        elif char == '-':
            nums.append(nums.pop(-2) - nums.pop(-1))
        elif char == '*':
            nums.append(nums.pop() * nums.pop())

print(nums[0])