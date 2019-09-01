name = str(input('What is your name? ')).strip()
check = "silva" in name.lower()

if check:
  print('true')
else:
  print('false')