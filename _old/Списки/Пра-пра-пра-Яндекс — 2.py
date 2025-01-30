base_list = []
search_list = []

n1 = int(input())
for i in range(n1):
    base_list.append(input())

n2 = int(input())
for i in range(n2):
    search_list.append(input())

results_list = base_list.copy()
for i in range(len(search_list)):
    for j in range(len(results_list), 0, -1):
        if not search_list[i] in results_list[j - 1]:
            del results_list[j - 1]

for elem in results_list:
    print(elem);