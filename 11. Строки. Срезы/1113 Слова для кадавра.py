template = input()
word = input()
nothing_to_eat = True
while word:
    is_ok = True
    finished = False
    if len(word) < len(template):
        word = input()
        continue
    for i in range(len(template)):
        if template[i] == '1' and word[i] not in 'бвгджзйклмнпрстфхцчшщ':
            is_ok = False
            break
        elif template[i] == '0' and word[i] not in 'аеёиоуыэюя':
            is_ok = False
            break
        elif template[i] == '*':
            right_part_len = len(template) - i -1
            template_right_part = template[-1 * right_part_len:]
            word_right_part = word[-1 * right_part_len:]
            for j in range(len(template_right_part)):
                if (template_right_part[j] == '1' and
                        word_right_part[j] not in 'бвгджзйклмнпрстфхцчшщ'):
                    is_ok = False
                    break
                elif (template_right_part[j] == '0' and
                      word_right_part[j] not in 'аеёиоуыэюя'):
                    is_ok = False
                    break
            finished = True
        if finished:
            break
    if is_ok:
        print(word)
        nothing_to_eat = False
    word = input()
if nothing_to_eat:
    print('Есть нечего, значить!')
