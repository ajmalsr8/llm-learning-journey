#small dataset management tool
#Required Features - Add Record, View Dataset, Search, Update, Delete, CSV Export, CSV Import and Dataset Statistics

import json
import os

JSON_File = "dataset.json"
CSV_File = "dataset.csv"

class Dataset_Manager:
    def __init__(self):
        self.dataset = []
        self.load_data()
    def load_data(self):
        
        if not os.path.exists(JSON_File):
            self.dataset=[]
            return
        try:
            with open(JSON_File,"r") as file:
                        self.dataset=json.load(file)
                        print(self.dataset)
        except json.JSONDecodeError:
            print("File is corrupted")
            self.dataset=[]
        except OSError:
            print("File not found")
            self.dataset=[]
    def save_data(self):
        try:
            with open(JSON_File,"w")as file:
                json.dump(self.dataset,file)
        except OSError:
            print("Unable to save data")
            
    def Add_Data(self):
        try:
            question= input("Enter the question : ")
            if not question:
                print("Please enter a valid input")
                return
        except OSError:
            print("Unable to add data")
            return
            
            
        try:
            answer= input("Enter the answer : ")
            if not answer:
                 print("Please enter a valid input")
                 return
        except OSError:
            print("Unable to add data")
            return
        try:
            catergory= input("Enter the category : ")
        except ValueError:
            print("Please enter a valid input")
            return
        if self.dataset:
            new_id= max(record["id"] for record in self.dataset)+1
        else:
            new_id=1
        record = {
            "id":new_id,
            "question":question,
            "answer":answer,
            "category":catergory
        }
        self.dataset.append(record)
        self.save_data()
        print("")
    def view_records(self):
        print("Data Set")
        if not self.dataset:
            print("Dataset is empty")
            return
        for record in self.dataset:
            print(f"ID : {record["id"]}")
            print(f"Question : {record["question"]}")
            print(f"Answer : {record["answer"]}")
            print(f"Category : {record["category"]}")
            
             
        
    
        
        
ob=Dataset_Manager()
ob.Add_Data()
# ob.load_data()
ob.view_records()

        
        
        
