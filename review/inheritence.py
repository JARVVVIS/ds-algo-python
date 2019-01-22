class Employee:
    raise_amout = 1.04 #class variable

    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@company.com"
    
    def fullname(self):
        return '{} + {}'.format(self.first,self.last)
    
    def apply_raise(self):
        self.pay  = int(self.pay*self.raise_amout)


class developer(Employee): #inherits employee class
    raise_amout = 1.10 #can change the raise amount in subclass without changing the parent class
    def __init__(self,first,last,pay,lang):
        super().__init__(first,last,pay) #will pass first,last,pay to the employee class
        self.lang = lang #sets up the language


class Manager(Employee):
    def __init__(self,first,last,pay,project):
        super().__init__(first,last,pay) #yeh sab employee se laa
        self.project = project



dev_1  = developer("ruchit" ,  "rawal" , 500000 , "c++")
dev_2 = developer("test" , "test" , 500000 , "python")
manager_1 = Manager("Ruchit" ,  "rawal" , 1000000 , "Coding project")


print(dev_1.email + dev_1.lang)
print(manager_1.__dict__)