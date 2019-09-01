trip = int(input('Distance? '))

if trip > 200:
  print('Price is: {0}'.format(trip*0.45))
else:
  print('Price is: {0}'.format(trip*0.50))