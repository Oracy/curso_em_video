import math
cat_op = float(input('Cateto Oposto: '))
cat_ad = float(input('Cateto Adjacente: '))
hipotenusa = round(math.hypot(cat_op, cat_ad), 2)

print('Hipotenusa de {0} e {1} = {2}'.format(cat_op, cat_ad, hipotenusa))