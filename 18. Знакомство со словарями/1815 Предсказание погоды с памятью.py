day0 = input()
p = float(input())
q = float(input())
days = int(input())

now = day0
forecast = {'ясно': 1, 'пасмурно': 1}

for _ in range(days):
    if now == 'ясно':
        forecast['ясно'] *= p
        forecast['пасмурно'] *= (1 - p)
    elif now == 'пасмурно':
        forecast['ясно'] *= (1 - q)
        forecast['пасмурно'] *= q
    now = max(forecast, key=forecast.get)

if forecast['ясно'] == forecast['пасмурно']:
    print('равновероятно')
else:
    print(now)
print(forecast[now])