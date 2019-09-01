speed = int(input('Speed? '))
bill = speed - 80

if speed > 80:
  print("""You are under arrested!!!
  Traffic Ticket R${0}.00""".format(bill * 7))
else:
  print('Have a good day!')
