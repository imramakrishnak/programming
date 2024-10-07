
class Employee1:
    pass

emp_1_1 = Employee1()
emp_2_1 = Employee1()

print(emp_1_1)
print(emp_2_1)

emp_1_1.firstName ="Ramakrishna"
emp_1_1.lastName = "Kommineni"
emp_1_1.email = "ramakrishna.kommineni@company.com"

emp_2_1.firstName ="Test"
emp_2_1.lastName = "User"
emp_2_1.email = "Test.User@company.com"

print(emp_1_1.email)
print(emp_2_1.email)

#--------------------------------------------------------------------

class Employee2:
    
    def __init__(self,firstName,lastName):
        self.firstName = firstName
        self.lastName = lastName
        self.email = firstName + lastName + '@company.com'

emp_1_2 = Employee2('Ramakrishna', 'Kommineni')
emp_2_2 = Employee2('Test', 'User')

print(emp_1_2.email)
print(emp_2_2.email)

#--------------------------------------------------------------------

class Employee3:

    def __init__(self,firstName,lastName):
        self.firstName = firstName
        self.lastName = lastName
        self.email = firstName + lastName + '@company.com'
    
    def fullname(self):
        return '{} {}'.format(self.firstName, self.lastName)

emp_1_3 = Employee3('Ramakrishna', 'Kommineni')
print(emp_1_3.fullname())
print(Employee3.fullname(emp_1_3))