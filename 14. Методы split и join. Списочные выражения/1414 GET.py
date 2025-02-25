url = input()
key = input()
tuplist = [tuple(tup.split('=')) for tup in url.split('?')[1].split('&')]
print(tuplist)

for t in tuplist:
    if t[0] == key:
        print(t[1])
