num = int(input('Type a number: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print("""Milhar: {0}
Centena: {1}
Dezena: {2}
Unidade: {3}""".format(m, c, d, u))
