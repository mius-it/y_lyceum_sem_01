import math

def gcd(a, b):
    """Вычисляет наибольший общий делитель (НОД) двух чисел."""
    while b:
        a, b = b, a % b
    return a

def find_primitive_pythagorean_triples(N):
    """Находит все примитивные пифагоровы тройки, где z <= N."""
    triples = set()  # Множество для хранения уникальных троек
    for m in range(1, int(math.sqrt(N)) + 1):
        for n in range(1, m):
            # Проверяем, что m и n взаимно просты и одно из них четное
            if gcd(m, n) == 1 and (m % 2 != n % 2):
                x = m**2 - n**2
                y = 2 * m * n
                z = m**2 + n**2
                # Проверяем, что z <= N
                if z <= N:
                    # Упорядочиваем тройку по возрастанию
                    triple = tuple(sorted((x, y, z)))
                    triples.add(triple)
    return triples

# Ввод данных
N = int(input("Введите число N: "))

# Находим примитивные пифагоровы тройки
triples = find_primitive_pythagorean_triples(N)

# Вывод результатов
for triple in sorted(triples):
    print(triple[0], triple[1], triple[2])