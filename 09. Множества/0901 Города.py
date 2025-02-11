N = int(input())
cities = set()
for i in range(N):
    cities.add(input())
if input() in cities:
    print('TRY ANOTHER')
else:
    print('OK')