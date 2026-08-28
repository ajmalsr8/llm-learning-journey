#Let Class as a blueprint
class Student:
    pass
#It defines what a Student object can be

#Creating an object
student1 =Student()
student2= Student()
#student1 and student2 are objects/instances of the Student class

#__init__
#Usually, we want an object to start with some information
class Student():
    def __init__(self,name,age): #when we call class Student then oython automatically calls init
        self.name=name #The self refers to the particular object we currently working with
        self.age=age
student1 = Student("Ajmal",27)
print(student1.name)
print(student1.age)
 
#example for self      
#when we execute another object,
student2=(Student("Sam",30))
print(student2.name) #init automatycally read argument value that passed through student2 to self.name=name


#Methods
#A method is a function belonging to a class
class Students ():
    def __init__(self,name,age):
        self.name=name 
        self.age=age
        
    def introduce(self):
        print(f"Hey my name is {self.name} and I'm {self.age} years old")
obj=Students("Ajmal",27)
obj.introduce()
#here self.name easly used in another method without passing arguments.

#Returning values from methods
class Claculator:
    def  add(self,a,b):
        return a+b
    def multiply(self,a,b):
        return a*b
calc_obj=Claculator()
print(calc_obj.add(5,8))
print(calc_obj.multiply(8,2))

#Instance attributes
class Car:
    def __init__(self,brand,model): #It means whwn we create an object the init fuction execute itself
        self.brand=brand
        self.model=model
        print(f" The car brand is {self.brand} and model is {self.model}")

car_obj=Car("Honda","Civic") #__init__ runs automatically 
car_obj=Car("Maruthi","Suzuki") #__init__ runs again

#Class attributes
#A class attribute is shared by instances unless overridden
#Defined directly inside the class and outside of __init__
#It is shared by all objects of the class unless we override it in a specific object
class Student_class:
    university="APJ University"  #class attribute
    def __init__(self,name):
        self.name= name     #instance attribute
#Each object gets its own copy, so student_att_01.name = "Ajmal" and student_att_02.name = "Alex" are different
student_att_01 = Student_class("Ajmal")
student_att_02 =Student_class("Alex")

print(student_att_01.university)
print(student_att_02.university)

#Inheritance (Important)
#Inheritance allows one class to inherit functionality from another

class Animal: #Parent class
    def speak(self):
        print("Animal make sound")
#Dog is child class
class Dog(Animal): #Dog inherits from Animal (parent class)
    def bark(self): 
        print("Dog barks") 
        
dog_obj=Dog() #create Dog object
dog_obj.bark() #calls Dog’s own method
dog_obj.speak() #calls inherited method from Animal

#Method overriding
#A child class can replace a parents method
class Animal_01:
    def speak(self):
        print("Some animal sound")
class Dog_01:
    def speak(self):
        print("Boww Boww")
class Cat:
    def speak(self):
        print("Meaww")

dog_obj=Dog_01()
cat_obj=Cat()
dog_obj.speak()
cat_obj.speak()


#Encapsulation
#Python doesn't enforce private variables in the same way as some languages, but we commonly use _ or __ conventions

class Bank_Account:
    def __init__(self,balance):
        self._balance = balance
         # _balance is the account's current money (private attribute)
    def withdrawal(self,amount):
        self._balance -=amount
        # subtracts money from _balance
    def get_balance(self):
        return self._balance
        # returns the current _balance
    def deposite(self,amount):
        self._balance += amount
        # adds money to _balance
bank_obj = Bank_Account(1000)
bank_obj.withdrawal(20)
print(bank_obj.get_balance())
bank_obj.deposite(60)
print(bank_obj.get_balance())
#hiding the balance inside the class and exposing only safe methods to interact with it
    
    
#Dataclasses (Important)
#This is especially useful for structured data
"""A dataclass in Python is essentially a shortcut for creating classes that are mainly used to store data. 
It automatically generates a lot of the repetitive boilerplate code for you."""

#Normally

""" class Student:
        def __init__(self, name, age, degree):
         self.name = name
         self.age = age
         self.degree = degree 
         
    Here, we must manually define __init__, and if we want __repr__ or __eq__, we need to write those too.
"""
#That's repetitive
#With a dataclass
from dataclasses import dataclass
@dataclass
class Student_d:
    name:str
    age:int
    height:float
st_obj=Student_d(name="Ajmal",age=27,height=173.5)
print(st_obj.name)

""" When to use dataclasses
✅ When class is mostly data storage (like models, records, configs).

❌ If class has complex behavior (lots of methods, not just attributes), a regular class may be better."""
  

#Dataclass with methods
from dataclasses import dataclass
@dataclass
class Profile:
    name : str
    age : int
    place : str
    
    def me(self):
        print(f"Hey my name is {self.name}.Im {self.age} years old,from {self.place}")
obb=Profile(name="Alex",age=24,place="Kulathupuzha")
obb.me()