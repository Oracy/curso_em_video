import math
angle = float(input('Type angle: '))
sin = round(math.sin(math.radians(angle)), 2)
cos = round(math.cos(math.radians(angle)), 2)
tan = round(math.tan(math.radians(angle)), 2)

print(""" Sin: {0}
Cos: {1}
Tan: {2}""".format(sin, cos, tan))