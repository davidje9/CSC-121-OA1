from employee import Employee

#create employee object
employee_one = Employee('David', 'Everson', 48000)
employee_two = Employee('Megan', 'Hoak', 58250)

#give employee a custom raise
employee_one.give_raise(17000)
employee_two.give_raise()

print(f"{employee_one.first} {employee_one.last}'s salary is now ${employee_one.salary}.")
print(f"{employee_two.first} {employee_two.last}'s salary is now ${employee_two.salary}.")
