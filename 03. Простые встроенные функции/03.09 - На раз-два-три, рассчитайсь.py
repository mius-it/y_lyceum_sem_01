boy1 = int(input())
boy2 = int(input())
boy3 = int(input())

if boy1 < boy2:
    boy1, boy2 = boy2, boy1
if boy1 < boy3:
    boy1, boy3 = boy3, boy1
if boy2 < boy3:
    boy2, boy3 = boy3, boy2

print(boy1)
print(boy2)
print(boy3)