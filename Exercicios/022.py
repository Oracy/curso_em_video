name = str(input('What is your full name? ')).strip()

upper = name.upper()
lower = name.lower()
count = len(name) - name.count(' ')
split = name.split(' ', 1)

print("""Name: {0}
Upper: {1}
Lower: {2}""".format(name, upper, lower))
print("Name {0} has {1} letters: ".format(name, count))
print('First name: {0}'.format(split[0]))