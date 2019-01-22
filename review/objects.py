# a class is the defination of data and methods for a specific type of object
#so class is like a custom datatype 
#object is just an instance of the class
#each class contains a constructer which initializes the instance
#self points to the current object , which will be known at time of declaring
#always first parameter while declaring a class methond is self


class Dog:
    #this is constructer , it will be called whenever a dog object will be created
    #self must be passed as first argument,note self is itself created by python so we just need to pass it
    def __init__(self,name,month,day,year,speakText):
        #these are the variables that will be passed while declaring
        self.name = name
        self.month = month
        self.day   = day
        self.year = year
        self.speakText = speakText 
        #note as self points to the object self. defines a property we can name it anything we want so that object can later acess it = name is the name variable being passed in the function argument
    
    #this is a method
    #note as this doesnt change the object its an accessor method
    def speak(self): 
        return self.speakText #it returns the siund spoken

    #this is a mutator method
    def changeName(self,new_name):
        self.name = new_name


boyDog =  Dog("Messe" , 2,12,1990,"Woof")
print(type(boyDog)) #should print dog type
print(boyDog.name) #name of dog
boyDog.changeName("Ronaldo")
print(boyDog.name)#the name after name is changed
