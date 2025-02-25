N = int(input())
recipe = []
for _ in range(N):
    string = input()
    if 'лук' not in string:
        recipe.append(string)
print(', '.join(recipe))
