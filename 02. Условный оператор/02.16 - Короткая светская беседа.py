print('Какое у тебя настроение?', end=' ')
answer = input()

if 'не' in answer or '?' in answer:
    print("Я просто программа и плохо понимаю человеческие чувства.")
else:
    if 'хорош' in answer or 'прекрасн' in answer or 'отличн' in answer:
        print('Я так рада, что у тебя всё хорошо!')
    elif 'плох' in answer or 'ужасн' in answer or 'отвратительн' in answer:
        print('Сожалею, что у тебя что-то не так. Всё наладится!')
    else:
        print("Я просто программа и плохо понимаю человеческие чувства.")