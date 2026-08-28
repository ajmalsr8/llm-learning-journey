#Bank Account


class Bank:
    def __init__(self,balance=100):
        self.username = None
        self.password = None
        self._balance = balance
        
    def create_account(self):
        print("============ CREATE ACCOUNT ================")
        
        username= input("Enter the your full name : ")
        password= input("Enter the password (must be numerics) :")
        
        if not username or not password:
                print("Error........ Enter valid input")
                return
        try:
            password = int(password)
        except ValueError:
            print("Error...........Password should be numeric")
            return
        
        self.username = username
        self.password = password 
        print("Account created sucessfully")
        print(f"Welcome {self.username}")   
       
    def login(self):
        print("============ LOGIN ================")
        if self.username is None:
            print("No account found. Please create an account first")
            return False
        username = input("Enter your username :")
        password = input("Enter your password :")
        
        try:
            password = int(password)
        except ValueError:
            print("Error.......... Password should be numeric")
            return False
        if username == self.username and password == self.password:
            print(f"Welcome {self.username}")
            return True
        else:
            print("Invalid username or password")
            return False    
    
    def withdrawal(self,amount):
        if amount<=0:
            print("Error.. Amount must be greater than zero")
            return
        if amount>self._balance:
            print("Insufficient balance")
            return
        
        self._balance -= amount
        print(f"Withdrawal successfull your current balance ₹{self._balance} ")
    
    def deposit(self,amount):
        if amount<0:
            print("Error.. Amount must be greater than zero")
            return
        self._balance += amount
        print(f"Deposit successfull your current balance ₹{self._balance} ")
    
    def check_balance(self):
        print(f"Avaliable balance is ₹{self._balance}")
        
  
        
    def user_acc(self):
        

        while True:  
            print("********************************************************")
            print("Press 1 for Balance check\nPress 2 for Withdrawal\nPress 3 for Deposite\nPress 4 for Exit")
            print("********************************************************")
                
            choice = int(input("Enter the input :" )) 
            if choice==1:
                self.check_balance()
            elif choice ==2:
                try:
                    amount= int(input("Enter the withdrawal amount :"))
                    self.withdrawal(amount)
                except ValueError:
                    print("Please enter a valid number.")
            elif choice==3:                
                try:
                    amount= int(input("Enter the Deposit amount :"))
                    self.deposit(amount)
                except ValueError:
                    print("Please enter a valid number.")
            elif  choice== 4:
                print("Exiting.....")
                break   
            else:
                print("Please enter a valid input (1-4)")  
        
    def main_menu(self):
        while True:
            print("\n")
            print("************************  Welcome to Bank of Kerala  ********************")
            print("********************************************************")
            print("Press 1 for Login\nPress 2 for create an account\nPress 3 for exit")
            print("********************************************************")
            try:
                choice = int(input("Enter a valid input: "))
            except ValueError:
                print("Please enter a number.")
                continue
            if choice == 1:
                if self.login():
                    self.user_acc()
                    
            elif choice==2:
                self.create_account()
                    
            elif choice==3:
                print("Thankyou..")
                break
            
ob=Bank()
ob.main_menu()







            