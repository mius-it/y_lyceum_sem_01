M = 4

library_set = {"Хоббит", "Алиса в стране чудес", "Том Сойер", "Остров сокровищ"}
print("В библиотеке 4 книги:", library_set)

N = 4
print("Проверь, есть ли в ней книги на лето.")

for i in range(N):
    print("Введи название книги:", end=' ')
    book = input()
    if book in library_set:
        print("YES")
    else:
        print("NO")