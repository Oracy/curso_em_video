text = str(input('Type phrase: ')).strip()

text = text.lower()
c = text.count('a')
first = text.find('a')
last = text.rfind('a')

print("""A letter appeared {0} times.
First position {1}
Last position {2}""".format(c, first+1, last+1))