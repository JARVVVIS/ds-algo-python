#depending on what objects we are working with '+' operator has diffrent behaviour 
#it adds 1+2=3 but concatenates in case of strings
#this is called operator overloading when operator is assigned to do diffrent work
#special methods are always surrounded by __ a.k.a dunder

class Employee:

    def __init__(self,first,last,pay):
        self.first = first 
        self.last = last
        self.pay = pay
        self.email =  first + "." + last + "@company.com"

    def fullname(self):
        return '{} + {}'.format(self.first,self.last)

    def __add__(self,other): #overloads the + operator
        return self.pay + other.pay
    
    def __len__(self): #total no. of characters in the full name
        return len(self.fullname())


emp_1 = Employee("Ruchit","Rawal",50000)
emp_2 = Employee("Test","test",100000)
print(emp_1+emp_2)
print(len(emp_1))