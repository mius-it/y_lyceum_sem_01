M = int(input())
canteen = set()
for i in range(M):
    canteen.add(input())

days = int(input())
for i in range(days):
    daydishes = int(input())
    for j in range(daydishes):
        canteen.discard(input())

for dish in canteen:
    print(dish)