n1 = float(input('First Rate: '))
n2 = float(input('Second Rate: '))

print('Your mean between \033[0;32m{0} \033[mand \033[0;32m{1} \033[mis: \033[1;31;43m{2}'.format(n1, n2, (n1+n2)/2))
