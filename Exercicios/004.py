word = input('Type something: ')

primate = type(word)
blank = word.isspace()
numeric = word.isnumeric()
alpha = word.isalpha()
alphanum = word.isalnum()
upper = word.isupper()
lower = word.islower()
cap = word.istitle()

print("""Primate: {0}
Blank? {1}
Number? {2}
Alpha? {3}
Alphanumeric? {4}
Upper? {5}
Lower? {6}
Cap? {7}""".format(primate, blank, numeric, alpha, alphanum, upper, lower, cap))
