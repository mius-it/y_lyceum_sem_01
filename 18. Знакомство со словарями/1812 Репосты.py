N = int(input())
posts = []
item = input()
itemtup = {'Author' : item[:item.find('опубликовал') - 1],
           'Views' : int(item[item.rfind(' ') + 1:])}
posts.append(itemtup)
print(posts)
for _ in range(N - 1):
    item = input()
    itemtup = {'Author': item[:item.find('опубликовал') - 1],
               'Views': int(item[item.rfind(' ') + 1:])}
    posts.append(itemtup)