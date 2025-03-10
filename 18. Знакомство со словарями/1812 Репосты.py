N = int(input())
posts = []
totalviews = [0] * N
item = input()
itemtup = {'Poster': item[:item.find('опубликовал') - 1],
           'Original': 'none',
           'Views': int(item[item.rfind(' ') + 1:])}
posts.append(itemtup)

for _ in range(N - 1):
    item = input()
    itemtup = {'Poster': item[:item.find('отрепостил') - 1],
               'Original': item[item.find('отрепостил пост у') + len('отрепостил пост у') + 1:item.find(',')],
               'Views': int(item[item.rfind(' ') + 1:])}
    posts.append(itemtup)

#print('\n'.join(str(p) for p in posts))

for i in range(N - 1, -1, -1):
    totalviews[i] += posts[i]['Views']
    for j in range(N - 1, i, -1):
        if posts[i]['Poster'] == posts[j]['Original']:
            totalviews[i] += totalviews[j]

print('\n'.join(str(t) for t in totalviews))
