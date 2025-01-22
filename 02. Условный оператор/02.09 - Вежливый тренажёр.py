print("Назовите себя, пожалуйста!")
name = input()
print("Введите текст.")
txt_01 = input()
print("Повторите текст.")
txt_02 = input()
if txt_01 == txt_02:
    print(name, ", введено верно!", sep='')
else:
    print(name, ", пока не получилось, попробуйте снова!", sep='')