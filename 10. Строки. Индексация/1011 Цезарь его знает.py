shift = int(input())
phrase = input()

for letter in phrase:
    order = ord(letter)
    if order >= 1040 and order <= 1071:
        order -= 1039
        order += shift
        order %= 31
        order += 1039
    elif order >= 1072 and order <= 1103:
        order -= 1071
        order += shift
        order %= 31
        order += 1071
    print(chr(order), end='')