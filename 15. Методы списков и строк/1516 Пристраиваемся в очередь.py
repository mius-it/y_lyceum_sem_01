N = int(input())
patients = []
for _ in range(N):
    phrase = input()
    if 'в очередь' in phrase:
        patients.append(phrase[:phrase.find(' ')])
    elif 'Привет' in phrase:
        surname = phrase[len('Привет, '):phrase.find('!')]
        for i in range(len(patients)):
            if patients[i] == surname:
                pos = i
                break
        patients.insert(pos + 1, phrase[phrase.find('!') + 2: -1 * len(' будет за тобой.')])
    elif 'хватит' in phrase:
        surname = phrase[:phrase.find(',')]
        patients.remove(surname)
print('\n'.join(p for p in patients))