n = int(input())
for _ in range(n):
    cubes = [int(c) for c in input().split()]
    pyramid = []
    while cubes:
        if cubes[0] >= cubes[-1]:
            next_cube = cubes.pop(0)  # Берем слева
        else:
            next_cube = cubes.pop()   # Берем справа
        if pyramid and next_cube > pyramid[-1]:  # Проверка на устойчивость
            print('НЕТ')
            break
        pyramid.append(next_cube)
    else:  # Если не было break
        print(' '.join(map(str, pyramid)))
