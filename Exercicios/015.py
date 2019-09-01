days = int(input('How many days? '))
km = float(input('How many kilometers? '))

days_price = days * 60
km_price = round(km * 0.15, 2)

print('You will pay: {0}'.format(days_price + km_price))