palettes = int(input())
uniques = set()
doubles = set()
cntr_all_colors = 0

for i in range(palettes):
    colors = int(input())
    for j in range(colors):
        col = input()
        if col not in uniques:
            uniques.add(col)
        else:
            doubles.add(col)
        cntr_all_colors += 1

print(len(doubles), cntr_all_colors - len(uniques & doubles))
