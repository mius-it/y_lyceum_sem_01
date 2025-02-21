soups = ['щи', 'борщ', 'щавелевый суп', 'овсяный суп', 'суп по-чабански']
days = int(input())
for i in range(days):
    print(soups[i % len(soups)])