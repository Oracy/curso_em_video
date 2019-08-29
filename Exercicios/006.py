import math

n = int(input('Type a number: '))

double = n*2
triple = n*3
square = round(math.sqrt(n), 2)

print("""Double is: {0}
Triple is: {1}
Square root is: {2}""".format(double, triple, square))
