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
            with open(JSON_File,"r",encoding="uft-8") as file:
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
            with open(JSON_File,"w",encoding="uft-8")as file:
                json.dump(self.dataset,file)
        except OSError:
            print("Unable to save data")
            
    def Add_Data(self):
        question= input("Enter the question : ")
        if not question:
            print("Please enter a valid input")
            return     
        answer= input("Enter the answer : ")
        if not answer:
            print("Please enter a valid input")
            return
        
        catergory= input("Enter the category : ")
        if not catergory:
            catergory = "Uncategorized"
            
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
            print("-"*20)
            
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
        key=input("Press any key to go back : ")
        if key:
            return
    
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
            with open(CSV_File,"w",newline="",encoding="utf-8") as file:
                        fieldname = ["id","question","answer","category"]
                        writer= csv.DictWriter(file,fieldnames=fieldname)
                        writer.writeheader()
                        writer.writerows(self.dataset)
                        print("Dataset Export Successfully")
                        
        except OSError :
            print("Error unable to export CSV file")
    def import_csv(self):
        if not os.path.exists(CSV_File):
            print("No files found")
            return
        try:
            with open(CSV_File,"r",newline="",encoding="utf-8") as file:
                reader = csv.DictReader(file)
                imported_records = []
                for row in reader:
                    record = { "id": int(row["id"]),
                            "question": row["question"],
                            "answer":row["answer"],"category":row["category"]}
                    
                    imported_records.append(record)
                self.dataset=imported_records
                self.save_data()
                print("Imported successfully")
        except OSError:
            print("Error")
            
    def statistics(self):
        print("Statistics")
        if not self.dataset:
            print("No records found")
            return
        total_records= len(self.dataset)
        categories = {}
        answers_length =[]
        for record in self.dataset:
            category=record["category"]
            categories[category]=(categories.get(category,0))+1
            answers_length.append(len(record["answer"]))
        print(f"Total Records {total_records}")
        
        print("Categories")
        for i,j in categories.items():
            print(f"Category : {i} -- Count :{j}")
        print("Average answer size")
        ans_size= sum(answers_length)/len(answers_length)
        print(f"Average answer size is {ans_size}")
        
        print(f"Longest Answer is {max(answers_length)} ")
        print(f"Shortest Answer is {min(answers_length)} ")
        
        
    def update_record(self):
        print("Update Record")
        
        if not self.dataset:
            print ("No records found")
            return
        try:
            record_id=int(input("Enter the record id :"))
        except ValueError:
            print("Input should be a number")
            return
        new_question = input("Enter the question (Press enter to keep old) : ")
        new_answer = input("Enter the answer (Press enter to keep old) : ")
        new_category = input("Enter the category (Press enter to keep old) : ")
        
        
        try:
            for record in self.dataset:
                if record_id == record["id"]:
                    if new_question:
                        record["question"] = new_question
                    if new_answer:
                        record["answer"] = new_answer
                    if new_category:
                        record["category"] = new_category
            print("Record Updated Successfully")
            self.save_data()
            return
        except OSError:
            print("Error")
                
            
                
            
            
    def main_menu(self):
        while True:
            print("*************************************************")
            print("=== DATASET MANGEMENT ===")
            print("Press 1 for View Records\nPress 2 for Load Data\nPress 3 for Add Data\nPress 4 for Search Data\nPress 5 for Delete Data\nPress 6 for Update Data\nPress 7 for Export to CSV File\nPress 8 for Import CSV File\nPress 9 for Statistics\nPress 10 for Exit\n")
            print("*************************************************")
            try:
                choice= int(input("Enter the Input : "))
            except ValueError:
                print("Input should be a number")
            if choice > 0 or choice<=10:
                if choice==1:
                    self.view_records()
                elif choice==2:
                    self.load_data()
                elif choice==3:
                    self.Add_Data()
                elif choice==4:
                    self.search()
                elif choice ==5:
                    self.delete()
                elif choice ==6:
                    self.update_record()
                elif choice==7:
                    self.exp_csv()
                elif choice==8:
                    self.import_csv()
                elif choice == 9:
                    self.statitics()
                elif choice== 10:
                    print("Exiting...........")
                    return
            else:
                print("Input value should be 1-9")
                          
            
                
        
            
             
        
    
        
        
ob=Dataset_Manager()
ob.main_menu()


        
        
        
