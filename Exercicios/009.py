n1 = int(input('Number to get all multiples: '))
n2 = int(input('Until which number do you want to calc? '))
x = 0

while x < n2:
  x+=1
  print('\033[0;34m{} \033[m* \033[0;34m{:2} \033[m= \033[0;32m{:2}'.format(n1, x, n1 * x))