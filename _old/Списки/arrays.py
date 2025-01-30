families = [['Папа', 'Мама', 'Саша', 'Матвей'],['Вадим', 'Света', 'Соня'],['Женя', 'Юля', 'Вася', 'Тося']]
print("Всё: ", families)

for i in range(len(families)):
    print(families[i])

for i in range(len(families)):
    for j in range(len(families[i])):
        print(families[i][j], "- молодец!")