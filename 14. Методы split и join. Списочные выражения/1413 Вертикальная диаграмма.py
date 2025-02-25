s = [int(n) for n in input().split()]
width = len(s) + 2
height = max(s) + 2

pic = [['.'] * width] * height

for h in range(height):
    for w in range(width):
        if (w == 0 or w == width - 1 or
            h == 0):
            pic[h][w] = '*'
        elif h > (height - s[w - 1] - 1):
            pic[h][w] = '*'
        else:
            pic[h][w] = ' '
        print(pic[h][w], end='')
    print()