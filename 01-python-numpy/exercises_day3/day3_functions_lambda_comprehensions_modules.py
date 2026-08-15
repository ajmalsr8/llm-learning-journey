#Function is a reusable block of code
def sample():  #simply define a function,
    print("Hello World") #add lines inside the function
    
sample() #function called, thus block of code inside the function starts execute 

#Parameters
#It means sending information when the function call
def sample_two(name): #here an rgument called "name" is used when function defining time
    print(f"Hello {name}") 
    
sample_two("Ajmal") #here Ajmal is the information/value that is send to the "name" (argument)

#Returning values
def add(a,b): #sending values to function
    return a+b #sends value back to the caller

result= add(2,5) #the value stored in a variable
print(result)

#Multiple parameters
def calculate_avrg(a,b,c):
    return (a+b+c)/3
avrg= calculate_avrg(23,41,20)
print(avrg)
    
    
#Default arguments
def def_arg(name="Ajmal"):
    print(f"Hello {name}")
    
def_arg() #Here is no arguments, so the function takes default argument
def_arg("Sooraj") #Here passing an argument to function so the function not take default argument

# *args
#Useful when we dont know how many positional arguments you'll receive
def total_sum(*numbers):  #if we dont know the number of arguments, then we can use it.
    return sum(numbers)

print(total_sum(5,4,8))
print(total_sum(62,14,56,32,14,78))


#**kwargs
#Used for variable keyword arguments

def show_info(**info):
    print(info)
    
show_info(name="Ajmal",
          age=27,
          height=5.8)
#get a dictionary like structure
#This becomes useful when working with configuration and API parameters later


#Lambda functions
#A lambda is a small anonymous function

#Normal function
def square(x):
    return x*x
print(square(5))

#Lambda
sq = lambda x:x*x
print(sq(6)) 

#Another example
sum = lambda d,f:d+f
print(sum(8,2))
#Important
#Dont use lambda everywhere
#For complicated logic, a normal def is usually clearer


#List comprehensions
#Normal approach
numbers = [2,3,4,5]
suqares = []

for number in numbers:
    suqares.append(number **2)
    
print(suqares)


#List comprehension
num=[7,8,9,10]
comp_square=[number **2 for number in num ]
print(comp_square)


#List comprehension with condition
nums=[1,2,3,4,5,6,7,8,9]
even_number = []
for i in nums:
    if i%2==0:
        even_number.append(i)
print(even_number)

#Comprehension
comp_num=[12,15,32,14,11]
comp_even=[ n for n in comp_num if n%2==0] #out [2,4,6,8]

print(comp_even)

#Dictionary comprehensions
#Normal way
List= [1,5,6,9,13,22] #declare a list
D_square={} #create an empty dict
for i in List: 
    D_square[i]= i**2 
print(D_square) #it gives out - 1:1 , 5:25 ,that number(key) and its square(value)

#Dictionary comprehension
C_List=[2,4,9,11]
D_C_square= {
    i:i**2
    for i in C_List  #all calculations done inside dict
}
print(D_C_square)

#Modules
#A module is simply a Python file containing code that can be imported elsewhere
import calculator #here we imported a python file that containing code
print(calculator.c_add(10,15)) #we used return in calculator.py file, so values sended from here to calculator.py execute the program and the result will return back to here
print(calculator.c_div(680,49)) 
print(calculator.c_mul(8,6))
print(calculator.c_sub(6,9))

# insted import calculator also use " from import calculator import c_add" so we can only import add function
 # in future we need to import files like this
# from tokenizer import tokenize
# from model import GPTModel
# from dataset import load_dataset