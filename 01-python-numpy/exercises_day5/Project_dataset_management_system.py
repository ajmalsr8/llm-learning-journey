#small dataset management tool
#Required Features - Add Record, View Dataset, Search, Update, Delete, CSV Export, CSV Import and Dataset Statistics

import json
import os
import csv

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
            
    def search(self):
        keyword=input("Enter the keyword to search :").strip().lower()
        if not keyword:
            print("Please enter a valid keyword")
            return
        flag=False
        for record in self.dataset:
            if  keyword in record["question"].lower() or keyword in record["answer"].lower() or keyword in record["category"].lower():
                print("\n === Serach successfully complete ===\n")
                print(f"ID {record["id"]}")
                print(f"Question : {record["question"]}")
                print(f"Answer : {record["answer"]}")
                print(f"Category : {record["category"]}")
                flag = True
        if not flag:
            print("No data found")
    
    def delete(self):
        print("\nDelete Record")
        try:
            delete_id = int(input("Enter the record id :"))
        except ValueError:
            print("\nRecord id should be a number")
            return
        for record in self.dataset:
            if delete_id==record["id"]:
                print(f"The question is {record["question"]}")

                print('\nAre you sure you want to delete this? ')
                confirm=input("Y/N ? :").lower()
                try:
                    if confirm=="y":
                        self.dataset.remove(record)
                        print("Successfully deleted")
                        self.save_data()
                        return
                    elif confirm=="n":
                        print("Delete Cancelled")
                        return
                except ValueError:
                    print("Please enter Y or N..")
                    return
            
        print("Please enter a valid record id")
        
    def exp_csv(self):
        print("CSV Exporting")
        if not self.dataset:
            print("No Records Found")
            return
        
        try:
            with open("CSV_File_EXP","w") as file:
                        fieldname = ["id","question","answer","category"]
                        writer= csv.DictWriter(file,fieldnames=fieldname)
                        writer.writeheader()
                        writer.writerows(self.dataset)
                        print("Dataset Export Successfully")
                        
        except OSError :
            print("Error unable to export CSV file")
            
            
                
        
            
             
        
    
        
        
ob=Dataset_Manager()
# ob.Add_Data()
# ob.load_data()
# ob.view_records()
# ob.search()
# ob.delete()
ob.exp_csv()


        
        
        
