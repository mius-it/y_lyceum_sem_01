import random
answer = ''

while answer != 'До свидания' and answer != 'Пока' and answer != 'Прощай':
    question_id = random.randint(1, 3)
    if question_id == 1:
        answer = input('Как твои дела? ')
        if 'хорош' in answer or 'прекрасн' in answer or 'отличн' in answer:
            print('Я так рада, что у тебя всё хорошо!')
        elif 'плох' in answer or 'ужасн' in answer or 'отвратительн' in answer:
            print('Сожалею, что у тебя что-то не так. Всё наладится!')
        else:
            print("Я просто программа и плохо понимаю человеческие чувства.")
    elif question_id == 2:
        answer = input('Как ты себя чувствуешь? ')
        if 'хорош' in answer or 'прекрасн' in answer or 'отличн' in answer:
            print('Молодец, так держать! Здоровье – наше всё!')
        elif 'плох' in answer or 'ужасн' in answer or 'отвратительн' in answer:
            print('Ой, как жаль. Может, обратиться к врачу?')
        else:
            print("Жаль, что я не пошла не медицинский: нечего посоветовать")
    elif question_id == 3:
        answer = input('Какие планы на вечер? ')
        if 'учить' in answer:
            print('Дело хорошее, знание - сила.')
        elif 'работ' in answer:
            print('Детский труд запрещён Конституцией РФ')
        elif 'игра' in answer:
            print('Игры развивают наше воображение. Главное - не переборщить.')
        elif 'спать' in answer:
            print('Выспаться никогда не повредит')
        else:
            print('Главное, чтобы тебе было хорошо')
