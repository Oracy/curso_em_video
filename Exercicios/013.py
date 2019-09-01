salary = float(input('Employee Salary? '))
raise_salary = float(input('Raise his salary in: '))
total = round(salary + salary * (raise_salary / 100), 2)

print('New salary is: {}'.format(total))