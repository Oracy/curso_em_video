from random import randrange
names = []
for n in range(4):
  names.append(input('Type names: {0} '.format(n+1)))

print("""Choice is: {0}""".format(names[randrange(4)]))
