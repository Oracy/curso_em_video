price = float(input('How much is that? '))
discount = float(input('Discount? '))
total = round(price - price*(discount/100), 2)

print('Product cost is: \033[0;33mR$ {0}\033[m, discount: \033[0;33m{1}%\033[m, total is: \033[0;31mR$ {2}'.format(
    price, discount, total))
