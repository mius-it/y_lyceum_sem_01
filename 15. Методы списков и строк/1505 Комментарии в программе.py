N = int(input()[1])

for _ in range(N):
    s = input()
    print(s[:s.find('#') if '#' in s else None].rstrip())