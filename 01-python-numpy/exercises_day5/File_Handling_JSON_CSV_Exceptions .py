#File Handling
"""
The basic pattern is
file = open("example.txt", "r")

#But the preferred approach is
with open("example.txt" ,"r") as file:
    content = file.read()
"""


#when we use 'with' Python automatically handles closing the file
"""
"r"	Read
"w"	Write
"a"	Append
"x"	Create new file
"""


#"w" — Write
with open("python.txt","w") as test:
    test.write("Hello Python")
    
# "r" — Read
with open("python.txt","r") as file:
    content = file.read()
print(content)

#"a" — Append
with open("python.txt","a") as file:
    file.write("\nHow are you(using append)") #Existing content remains, and the new content is added.
#read
with open("python.txt","r") as file:
    content = file.read()
print(content)



#Part 2 — Reading Files
'''There is three important methods
read()
Reads everything'''

#readline()
#Reads one line
with open("python.txt","r")as file:
    sample=file.readline()
print(sample)

#readlines()
#Reads lines into a list
with open("python.txt","r")as file:
    lines=file.readlines()
print(f"readlines : {lines}")

"""
why this matter for LLMs?
resume.pdf
     ↓
Extract text
     ↓
Process text
     ↓
Create chunks
     ↓
Create embeddings
     ↓
Store in vector database

file handling isn't just basic Python knowledge. It's part of the infrastructure around ML/LLM systems

"""

#Part 3 — JSON
#JSON is extremely important for LLM engineering
#JSON is look like this
{
    "name": "Ajmal",
    "age": 27,
    "skills": ["Python", "C", "Flutter"]
}
#Python → JSON   Called serialization
import json
data = {
    "name": "Ajmal",
    "skills": ["Python", "LLM"]
}

json_string = json.dumps(data)

print(json_string)

#JSON → Python  Called deserialization
json_data = json.loads(json_string)
print(json_data["name"])

#write to json file
new_json_file={"name":"Jojo"
               ,"age":28,
               "Job":"Driver"}
with open("new_json.json","w") as abc:
    json.dump(new_json_file,abc)
with open("new_json.json","r")as efg:
    json_read=json.load(efg)
print(json_read)

'''
json.dumps() -- works with a string
json.dump() -- writes to a file
json.loads() -- reads a JSON string
json.load() -- reads from a file
'''

#Part 4 — CSV (Comma Separated Values)

"""
Example:

name,age,language
Ajmal,27,Python
Rahul,25,Java
Anu,24,C++

Python has a built-in csv module """

#Reading CSV
import csv
with open("student.csv","r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
    
# Part 5 — Exceptions
"""
number = int(input("Enter number: "))
If the user enters: hello
Python raises: value error
Without handling it, our program crashes
with try execpt
"""

# example
"""a= int(input("enter a number : "))
print(a)

this will make error"""

try:
    a=int(input("Enter a number :"))
except ValueError:
    print("Error.....The value should be a number")
    
"""try:
    # risky code

except SomeError:
    # handle error

else:
    # runs if no error

finally:
    # always runs
    """
# Example
try:
    number = int(input("Enter number: "))

except ValueError:
    print("Invalid input")

else:
    print(f"You entered {number}")

finally:
    print("Program finished")
