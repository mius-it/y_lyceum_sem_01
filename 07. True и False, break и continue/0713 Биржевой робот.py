price_yesterday = price_buy = price_sell = 0
is_bought = is_sold = False
price = int(input())
while price:
    if not is_sold:
        if price_yesterday == 0:
            is_bought = is_bought
        elif price > price_yesterday and not is_bought:
            is_bought = True
            price_buy = price
        elif price < price_yesterday and is_bought:
            is_sold = True
            price_sell = price
    price_yesterday = price
    price = int(input())
print(price_buy, price_sell, price_sell - price_buy)