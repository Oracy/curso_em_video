meters = float(input('Distance in meters: '))

km = meters/1000
hm = meters/100
dam = meters/10
dm = round(meters*10)
cm = round(meters*100)
mm = round(meters*1000)

print("""\033[0;32m{0} \033[mIs the same as:
\033[0;32m{1} \033[mkm
\033[0;32m{2} \033[mhm
\033[0;32m{3} \033[mdam
\033[0;32m{4} \033[mdm
\033[0;32m{5} \033[mcm
\033[0;32m{6} \033[mmm""".format(meters, km, hm, dam, dm, cm, mm))
