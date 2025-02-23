n = int(input())
list_tup = []

for i in range(n):
    line = input()
    points = int(input())
    tup1 = (line, points)
    list_tup.append(tup1)

list_points = []
for i in range(n):
    list_points.append(list_tup[i][1])
list_points.sort()

list_points_loose = list_points[:n // 2]
list_points_win = list_points[n // 2:]

list_names_win = []
for i in range(len(list_points_win)):
    for j in range(n):
        if list_points_win[i] == list_tup[j][1]:
            list_names_win.append(list_tup[j][0])
            break
list_names_win.sort()

list_names_loose = []
for i in range(len(list_points_loose)):
    for j in range(n):
        if list_points_loose[i] == list_tup[j][1]:
            list_names_loose.append(list_tup[j][0])
            break
list_names_loose.sort()

for s in list_names_win:
    print(s)
for s in list_names_loose:
    print(s)
