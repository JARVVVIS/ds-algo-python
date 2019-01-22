class Employee:

    def __init__(self,first,last):
        self.first = first
        self.last = last
    

    @property #getter
    def email(self):
        return '{}.{}@email.com'.format(self.first,self.last) #now we can use this method as an attribute
    
    @property
    def fullname(self):
        return '{} {}'.format(self.first,self.last)
    
    @fullname.setter #sets the first name and last name according to fullname entered
    def fullname(self,name):
        first,last = name.split(' ')
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        print("Name Deleted!")
        self.first = None
        self.last = None

emp_1 = Employee("Ruchit","Rawal")
print(emp_1.fullname)#use as an  attribute
emp_1.fullname = "Jon Snow" #use the setter
del emp_1.fullname #delete