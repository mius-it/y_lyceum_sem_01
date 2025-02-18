set_result = set()
set_temp = set()
set_doubles = set()

string = input()
while string:
    num = int(string)
    while num != -1:
        set_temp.add(num)
        num = int(input())
    set_doubles = (set_result & set_temp) | set_doubles
    if len(set_result):
        set_result = (set_result ^ set_temp) - set_doubles
    else:
        set_result = set_temp.copy()
    set_temp.clear()
    string = input()

for i in set_result:
    print(i, end=' ')
