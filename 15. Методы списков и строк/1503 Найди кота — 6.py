N = int(input())
for i in range(N):
    string = input()
    if 'кот' in string:
        print(i + 1, string.find('кот') + 1)