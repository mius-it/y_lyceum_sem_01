s = input()
length = 0
while 'Гэндальф' not in s:
    if 'волшебн' in s:
        length += len(s)
    s = input()
print(length)