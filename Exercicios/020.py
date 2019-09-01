from random import shuffle
names = []
for n in range(4):
  names.append(input('Type names: {0} '.format(n+1)))
shuffle(names)
print(names)
