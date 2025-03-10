N = int(input())
posts = []
item = input()
itemtup = {'Author' : item[:item.find('опубликовал') - 1],
           'Reposter': 'none',
           'Views' : int(item[item.rfind(' ') + 1:])}
posts.append(itemtup)

for _ in range(N - 1):
    item = input()
    itemtup = {'Author': item[item.find('отрепостил пост у') + len('отрепостил пост у') + 1:item.find(',')],
               'Reposter': item[:item.find('отрепостил') - 1],
               'Views': int(item[item.rfind(' ') + 1:])}
    posts.append(itemtup)

print('\n'.join(str(p) for p in posts))

for i in range(N):
    views = 0
    views += posts[i]['Views']
    print(views)
