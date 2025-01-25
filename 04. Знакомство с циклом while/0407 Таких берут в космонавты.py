str = input()
min = int(str)
max = 0
valid = 0

while str != '!':
    height = int(str)
    if height >=150 and height <=190:
        valid += 1
        if height > max:
            max = height
        if height < min:
            min = height
    str = input()
print(valid)
print(min, max)