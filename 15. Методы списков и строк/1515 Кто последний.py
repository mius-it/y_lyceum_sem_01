N = int(input())
patients = []
for _ in range(N):
    phrase = input()
    if 'Кто последний?' in phrase:
        patients.append(phrase[len('Кто последний? Я - '):-1])
    elif 'Я только спросить!' in phrase:
        patients.insert(0, phrase[len('Я только спросить! Я - '):-1])
    else:
        if patients:
            print('Заходит ', patients.pop(0), '!', sep='')
        else:
            print('В очереди никого нет.')