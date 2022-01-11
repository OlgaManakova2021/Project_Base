# в интернет-магазине сегодня 10% скидка на ряд товаров

price = [500, 1200, 800, 600, 150]
price_new = [n * (1 - 0.1) for n in price]

print('Старый прайс',price)
print('Новый прайс', price_new)

price_new1 = [n * (1 - 0.1) for n in price if n < 1000]
print('Новый прайс со стоимостью менее 1 тыс. руб.', price_new1)
