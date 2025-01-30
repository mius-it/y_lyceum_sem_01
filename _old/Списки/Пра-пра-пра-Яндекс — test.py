
#'''
base_list = ["сериал шерлок смотреть онлайн",
    "учебник питона",
    "мемы",
    "социальная сеть",
    "упражнения по питону",
    "кормовые мыши для питонов",
    "ответы егэ скачать бесплатно",
    "компьютерные мыши"]
search_list = ["питон", "мыши"]
n1 = 8
n2 = 2
#'''



'''
base_list = []
search_list = []

print("Введите количество строк базы:")
n1 = int(input())
print("Введите строку базы:")
for i in range(n1):
    if i > 0:
        print("Ещё одну:")
    base_list.append(input())

print("Введите количество поисковых строк:")
n2 = int(input())
print("Введите поисковую строку:")
for i in range(n2):
    if i > 0:
        print("Ещё одну:")
    search_list.append(input())
'''
print("База:", base_list)
print("Поиск:", search_list)

results_list = base_list.copy()
for i in range(len(search_list)):         #Перебираем search_list
    for j in range(len(results_list), 0, -1):     #Перебираем results_list
        if not search_list[i] in results_list[j-1]:
            del results_list[j-1]

print("Результат:", results_list)