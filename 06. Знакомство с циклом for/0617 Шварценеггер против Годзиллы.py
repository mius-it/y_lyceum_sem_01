pellets = int(input())
damage_numerator = 0
damage_denominator = 0

for i in range(pellets):
    pellet_numerator = int(input())
    pellet_denominator = int(input())
    if damage_numerator == 0:
        damage_numerator = pellet_numerator
        damage_denominator = pellet_denominator
    else:
        damage_numerator = (damage_numerator * pellet_denominator +
                            pellet_numerator * damage_denominator)
        damage_denominator = damage_denominator * pellet_denominator
        a = damage_denominator
        b = damage_numerator
        r = a % b
        while r != 0:
            a,b = b,r
            r = a % b
        nod = b
        damage_numerator /= nod
        damage_denominator /= nod
print(int(damage_numerator), '/', int(damage_denominator), sep='')