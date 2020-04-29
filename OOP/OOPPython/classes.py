# Python Object-Oriented Programming
#the instance goes as argument by default
import datetime as dt
class Employee:#Blueprint to create instances

    raise_amount = 1.04 # -> class variable
    number_of_emps = 0
    
    def __init__(self, first, last, pay):#instance as first method. self name as convencion
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first+'.'+last+'@company.com'
    
        Employee.number_of_emps += 1#constant class value, no need for each istance to have acess to it
        
    def fullname(self):#self means instance as first parameter
        return '{} {}'.format(self.first,self.last)    
        
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount) #or Employee.raise_amount, self.raise_amount allows you to change the raise amount for each employ
       
    @classmethod #Alter functionality to receive class as argument. Works with the class instead of the instace
    def set_raise_amt(cls, amount):
        cls.raise_amount = amount
        
    @classmethod #Alter functionality to receive class as argument. Works with the class instead of the instace
    def from_string(cls, emp_str):#classmethod as alternative contrustor
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)
        
    @staticmethod#Should be statis if you dont acess any part of the class/instance on the method
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True
    
    def __repr__(self): #unabiguous method used for debbuging (?)
        return "Employee('{}','{}', {})".format(self.first, self.last, self.pay)
    
    def __str__(self):
        return "Employee('{}','{}')".format(self.fullname, self.email)
    
    def __add__(self, other):
        return self.pay + other.pay
    
class Developer(Employee):#inheretance of Employee
    
    raise_amount = 1.10

    def __init__(self, first, last, pay, prog_lang):#extra argument for developer programming language
        super().__init__(first, last, pay)#uses employ __init__ method
        self.prog_lang = prog_lang
        
        
class Manager(Employee):#inheretance of Employee
    
    raise_amount = 1.10

    def __init__(self, first, last, pay, employees = None):#extra argument for developer programming language
        super().__init__(first, last, pay)#uses employ __init__ method
        if employees is None:
            self.employees = []
        else:
            self.employees = employees
            
    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)
            
    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)
        
    def print_emps(self):
        for emp in self.employees:
            print(' -> ',emp.fullname())# every emp is an instance of Employee
            
        
           
#%%   
emp_1 = Employee('Marcio','Coltro',6000)
emp_2 = Employee('Marcio2','Coltro2',5000)

emp_1.fullname()#-> no need for params since instance goes by default
Employee.fullname(emp_1)#-> need params since class dont know which isntace it should apply the function to

emp_1.apply_raise()
emp_1.pay

emp_1.raise_amount = 1.05 #-> changes only for the instance of the class
Employee.raise_amount = 1.05#-> changes for all instances

#all values of instances/classes
print(emp_1.__dict__)
print(Employee.__dict__)

print(Employee.number_of_emps)

#ClassMethods
Employee.set_raise_amt(1.05)

emp_string_1 = 'Marcio-Coltro-6600'
new_empl = Employee.from_string(emp_string_1)

##normal methods pass self as argument, classmethods pass class as argument, staticmethods dont pass anything
print(emp_1.is_workday(dt.datetime.today())) #is today workday?
#%%
print(help(Developer))#Usefull shit

dev_1 = Developer('Marcio','Coltro',6000,'Python')
dev_2 = Developer('MR.','falcatrua',6000,'Javascript')

dev_1.apply_raise()#changes the raise of developers to 10% while still using all the atributs and methods of the other classes
print(dev_1.pay,dev_1.email,dev_1.prog_lang)


man_1 = Manager('Test','Test',5000,[dev_1])
man_1.add_emp(dev_2)
print(man_1.email,man_1.print_emps())

print(isinstance(man_1,Developer))

print(issubclass(Manager,Employee))

##Dunder magic
# underscores before and after are named DUNDER
print(repr(emp_1))# prints different becuse the __repr__ method
print(str(emp_1))


print(emp_1+emp_2)#-> works becuse of the dunder method __add__


## what if the last name of the employee changes and you want to update the email as well
#reimplementation of class for reasons
class Employee:#Blueprint to create instances

   
    def __init__(self, first, last, pay):#instance as first method. self name as convencion
        self.first = first
        self.last = last
        self.pay = pay
       # self.email = first+'.'+last+'@company.com'
    @property #removes the self.email and transforms this method into a class property
    def email(self):
        return '{}.{}@company.com'.format(self.first,self.last)
        
    @property
    def fullname(self):#self means instance as first parameter
        return '{} {}'.format(self.first,self.last)    
        
    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last
        
    @fullname.deleter
    def fullname(self):
        print('delete the names')
        self.first = None
        self.last = None
        
emp_1 = Employee('Marcio','Coltro',6000)
emp_2 = Employee('Marcio2','Coltro2',5000)

emp_1.last = 'falcatrua'#updates last name
print(emp_1.email) # prints marcio.falcatrua@company.com

emp_1.fullname = 'Marcio Coltro'#uses fullname setter
print(emp_1.email) # prints marcio.falcatrua@company.com

del emp_1.fullname
