cnt_good = 0
cnt_evil = 0
last_phrase = ""

while 1:
    phrase = input()
    if phrase == "добрый":
        last_phrase = phrase
        cnt_good += 1
    elif phrase == "злой":
        last_phrase = phrase
        cnt_evil += 1
    elif phrase == "Какой подарок?":
        if cnt_good > cnt_evil and last_phrase == "добрый":
            print("серебряный шиллинг")
        elif cnt_good < cnt_evil and last_phrase == "злой":
            print("золотой")
        else:
            print("Ах, не знаю!")
            break
        cnt_good = 0
        cnt_evil = 0
    elif phrase == "":
        break