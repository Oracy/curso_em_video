name = str(input('Type your full name: ')).strip()

name = name.split(' ')
size = len(name)
first = name[0]
last = name[size-1]

print("""First Name: {0}
Last Name: {1}""".format(first, last))