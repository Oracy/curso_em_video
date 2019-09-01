from random import randint

pc_num = randint(0, 5)
num = -1

while num != pc_num:
  num = int(input('Type number: '))

  if(num == pc_num):
    print('Congratz you win!')
  else:
    print('YOAW!! I win!!!!')