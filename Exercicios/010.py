money = float(input('How much money do you have on your wallet? R$'))

usd = 0.24

print('With \033[0;32m{0} \033[myou can buy only \033[0;31m{1} \033[mUSD'.format(money, money * usd))