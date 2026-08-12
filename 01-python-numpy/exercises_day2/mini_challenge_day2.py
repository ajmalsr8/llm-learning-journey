students={    #create dict called students
    
    "Ajmal":{  #here Ajmal Anoob and Rahul are key
    "age":27,
    "degree": "BTech in ECE",
    "year": 2024,
    "course completion" :"yes" #Each value is another dictionary with details like age, degree, year, and course completion status.
},

"Anoob":{
    "age":29,
    "degree": "BTech in CSE",
    "year": 2024,
    "course completion" :"no"
},

"Rahul":{
    "age":28,
    "degree": "BTech in ME",
    "year": 2024,
    "course completion" :"yes"
},
}
#This is a nested dictionary: a dictionary inside another dictionary.
for name,details in students.items(): #Returns pairs of (key, value) from the dictionary.Name will hold the students name like "Ajmal"
    if details["course completion"]=="yes": #details will hold the inner dictionary like {"age": 27, "degree": ..., "course completion": "yes"}.
        print(name) 