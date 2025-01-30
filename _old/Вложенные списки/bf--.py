my_list = [0] * 30000
my_index = 0
print("+++.[" + "\033[34m>" + "\033[37m----")
line_com = input()
for i in range(len(line_com)):
    if '+' in line_com[i]:
        my_list[my_index] += 1
        if my_list[my_index] == 256:
            my_list[my_index] = 0
    if '-' in line_com[i]:
        my_list[my_index] -= 1
        if my_list[my_index] == -1:
            my_list[my_index] = 255
    if '>' in line_com[i]:
        my_index += 1
        if my_index == 30000:
            my_index = 0
    if '<' in line_com[i]:
        my_index -= 1
        if my_index == -1:
            my_index = 29999
    if '.' in line_com[i]:
        print(my_list[my_index])