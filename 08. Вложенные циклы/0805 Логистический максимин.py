roads = int(input())
best_road = 0
min_height = max_min_height = 0

for i in range(1, roads + 1):
    tunnels = int(input())
    for j in range(tunnels):
        height = int(input())
        if min_height > 0:
            if min_height > height:
                min_height = height
        else:
            min_height = height
    if max_min_height > 0:
        if max_min_height < min_height:
            max_min_height = min_height
            best_road = i
    else:
        max_min_height = min_height
        best_road = i
    min_height = 0
print(best_road, max_min_height)