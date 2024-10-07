class Employee1:

    raise_amount = 1.04
    no_of_employees = 0

    def __init__(self, firstName, lastName, pay):
        self.firstName = firstName
        self.lastName = lastName
        self.email = firstName + lastName + '@company.com'
        self.pay = pay
        Employee1.no_of_employees = Employee1.no_of_employees + 1

    def fullname(self):
        return '{} {}'.format(self.firstName, self.lastName)

    def apply_raise(self):
        self.pay = int(self.pay * Employee1.raise_amount)
        self.pay = int(self.pay * self.raise_amount)

emp_1_1 = Employee1('Ramakrishna', 'Kommineni', 50000)

print(emp_1_1.pay)
emp_1_1.apply_raise()
print(emp_1_1.pay)

print(Employee1.raise_amount)
print(emp_1_1.raise_amount)

print(Employee1.__dict__)
print(emp_1_1.__dict__)

Employee1.raise_amount = 1.05

print(Employee1.raise_amount)
print(emp_1_1.raise_amount)

emp_1_1.raise_amount = 1.06

print(Employee1.raise_amount)
print(emp_1_1.raise_amount)

print(Employee1.__dict__)
print(emp_1_1.__dict__)

print(Employee1.no_of_employees)