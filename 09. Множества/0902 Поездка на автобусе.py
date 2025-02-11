list1 = set();
list2 = set();

num = input()
while num != '':
    list1.add(num)
    num = input()
num = input()
while num != '':
    list2.add(num)
    num = input()

list3 = list1 & list2
if list3:
    for num in list3:
        print(num)
else:
    print('EMPTY')