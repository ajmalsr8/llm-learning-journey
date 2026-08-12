#Data Types
name = '"Ajmal' #String
age = 27 #Integer
height = 5.8 #Float
learning = True #Boolean

print(type(name))
print(type(age))
print(type(height))
print(type(learning))

#Basic Operators
a=10
b=5
print(a+b) #Addition
print(a-b) #Subtraction
print(a*b) #Multiplication
print(a/b) #Division
print(a//b) #Floor division
print(a%b) #Remainder
print(a**b) #Power


#Conditions
#Simple if-else condition
age=27
if age>=18:
    print("Adult")
else:
    print("Not an adult")
    
#elif case
score=76

if score >=90:
    print("Excellent")
elif score >=75:
    print("Good")
elif score>=50:
    print("Pass")
else:
    print("Fail")
    
    
#Lists
language=["Python","C","Dart","Java"]
print(language[2])
print(language[1])
#Append & Remove
language.append("C#") 
language.remove("Dart")
print(language)


#Dictionaries
student = {
    "name":"Ajmal", #key value pair
    "degree":"B.Tech ECE",
    "year": "2024"
}
print(student["name"])
print(student["year"])
# This becomes useful later when dealing with:JSON, API responses, datasets, model configurations

#Loops

#for
languages=["python","C","Dart","Java"]
for i in languages:
     print(i)
     
#range
for i in range(5): #here i value changes from 0 to 4
    print(i) 
    
#while
count=0 #initially count is 0
while count<10: #1st  iteration check count (0) < 10, its true, then enters to the loop
    print(count) #print 0
    count +=count #increment count +1 then again go back to while loop 