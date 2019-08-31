width = float(input('Wall\'s width: '))
height = float(input('Wall\'s height: '))

print('Wall\'s dimmension is: {}x{}, your total area is: {}m2'.format(width, height, width * height))
print('To paint your wall is necessary {} liters'.format((width*height)/2))