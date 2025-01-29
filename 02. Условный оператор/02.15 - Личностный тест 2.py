print('Какое ваше любимое время года: весна, лето, осень или зима?', end=' ')
question01 = input()

if (question01 == 'весна' or question01 == 'лето' or
        question01 == 'осень' or question01 == 'зима'):
    print('Каких животных вы любите больше: котиков, собачек, хомяков?', end=' ')
    question02 = input()

    if (question02 == 'котиков' or question02 == 'собачек' or
            question02 == 'хомяков'):
        if question01 == 'весна' and question02 == 'котиков':
            print('В душе Вы весенний котик.')
        elif question01 == 'весна' and question02 == 'собачек':
            print('В душе Вы весенняя собачка.')
        elif question01 == 'весна' and question02 == 'хомяков':
            print('В душе Вы весенний хомяк.')
        elif question01 == 'лето' and question02 == 'котиков':
            print('В душе Вы летний котик.')
        elif question01 == 'лето' and question02 == 'собачек':
            print('В душе Вы летняя собачка.')
        elif question01 == 'лето' and question02 == 'хомяков':
            print('В душе Вы летний хомяк.')
        elif question01 == 'осень' and question02 == 'котиков':
            print('В душе Вы осенний котик.')
        elif question01 == 'осень' and question02 == 'собачек':
            print('В душе Вы осенняя собачка.')
        elif question01 == 'осень' and question02 == 'хомяков':
            print('В душе Вы осенний хомяк.')
        elif question01 == 'зима' and question02 == 'котиков':
            print('В душе Вы зимний котик.')
        elif question01 == 'зима' and question02 == 'собачек':
            print('В душе Вы зимняя собачка.')
        elif question01 == 'зима' and question02 == 'хомяков':
            print('В душе Вы зимний хомяк.')
    else:
        print('Неверный ответ')
else:
    print('Неверный ответ')