#Part A — Functions
#Function with argument with return value

#area calculation

length= int(input("Enter the length in cm :"))
width= int(input("Enter the width in cm :"))
def area_calculation(a,b):
    result = a*b
    return result

print(f"Area is {area_calculation(length,width)} cm.")


# Part B — Lambda

# Create a lambda that calculates the cube of a number.
cube = lambda i:i**3
print(cube(3))     
 
 
# Part C — List comprehension
#Square

List=[1,2,3,4,5,6]
square=[i**2
    for i in List]

print(square)

#Even number
#using same list
even_number=[i for i in List
             if i%2==0]
print(even_number)


# Part D — Dictionary comprehension
#using same list
dict_sqr={i:i**2 for i in List}
print(dict_sqr)
