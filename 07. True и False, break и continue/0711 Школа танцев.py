tolerance = int(input())
while tolerance:
    cntr = 0
    rhythm_prev = ''
    while 1:
        rhythm = input()
        if rhythm == 'раз' and (rhythm_prev == 'четыре' or rhythm_prev == ''):
            cntr += 1
            rhythm_prev = rhythm
        elif rhythm == 'два' and rhythm_prev == 'раз':
            cntr += 1
            rhythm_prev = rhythm
        elif rhythm == 'три' and rhythm_prev == 'два':
            cntr += 1
            rhythm_prev = rhythm
        elif rhythm == 'четыре' and rhythm_prev == 'три':
            cntr += 1
            rhythm_prev = rhythm
        else:
            print('Правильных отсчётов было', cntr, ', но теперь вы ошиблись.')
            break
    tolerance -= 1
print('На сегодня хватит.')