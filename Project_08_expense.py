#Programm for Create a Ledger Book for a person in certain month Expenses(Adding new ledgerbook each month,addingexpense,View Expenses History)
class Expenses:
    
    
    def __init__(self):
        self.LedgerBookSerialNumber = ""
        self.LedgerBookHolderName = ""
        self.Capital = 0
        self.ExpenseAmount = 0
        self.BalanceAmount = 0
        self.Mobile = ""
        self.choice = 0
        self.contine = True
    def your_choice(self):
            try:

                self.choice = 0
                print("")
                self.choice = int(input("1)Open a new LedgerBook\n\n2)Expense\n\n3)View Transaction History\n\nenter your choice:- "))
                if   self.choice == 1:
                     self.CreatingNewLedgerBook()
                elif self.choice == 2:
                     self.Expense()
                elif self.choice == 3:
                     self.view_transaction()
                else:
                    print("You enterd wrong choice please enter any of this choice \n1)Open a new Account\n2)withdraw\n3)View Transaction History")
            except ValueError:
                print("Invalid input Please enter integer number only")
    
    def CreatingNewLedgerBook(self):
        try:
            self.LedgerBookHolderName = input("Enter your Name:- ")
            self.Month = input("enter the Month:- ")
            self.LedgerBookSerialNumber = f'{self.LedgerBookHolderName}'+f'-{self.Month}'           
            self.Capital = int(input("enter the capital Amount for opening the Ledger Book:- "))
            self.BalanceAmount = self.Capital
            print(f"Welcome {self.LedgerBookHolderName} You opened an Ledger Book Successfuly with Capital Amount of Rs.{self.Capital}/-. \nPlease note {self.LedgerBookSerialNumber} is your Ledger Book Serial number")
            with open(f"{self.LedgerBookSerialNumber}.txt",'w') as f:
                f.write(f"\t\tExpense of {self.LedgerBookHolderName} in {self.Month}\n\n\n Welcome {self.LedgerBookHolderName} You opened an Ledger Book with Capital Amount of Rs.{self.Capital}/-. \nAccount number:- {self.LedgerBookSerialNumber}\nBalance= Rs.{self.BalanceAmount}\n")
        except ValueError:
            print("Invalid input please enter An integer")
    
    
    def Expense(self):
        
        try:
            self.LedgerBookSerialNumber=input("Enter Ledger Book Serial Number:- ")
            while True:
                self.Prodct=input("Enter the Product that you want to buy:- ")
                self.ExpenseAmount=int(input("Enter the Expense of that Product:- "))
                
                #programm for fetching Balance
                with open(f"{self.LedgerBookSerialNumber}.txt", 'r') as f:
                    lines = f.readlines()

                balance_line = None
                for line in lines:
                    if line.startswith('Balance= Rs.'):
                        balance_line = line
                        break

                if balance_line:
                    balance_value = balance_line.split('= Rs.')[1].strip()
                    self.BalanceAmount=int(balance_value)
                else:
                    print("Balance not found")
                #....................end..................................
                
                self.BalanceAmount=self.BalanceAmount-self.ExpenseAmount
            
                #programm for updating balance for fetching
                with open(f"{self.LedgerBookSerialNumber}.txt", 'r') as f:
                    lines = f.readlines()

                with open(f"{self.LedgerBookSerialNumber}.txt", 'w') as f:
                    for line in lines:
                        if line.startswith('Balance= Rs.'):
                            f.write(f'Balance= Rs.{self.BalanceAmount}\n')  # Replace with the new value you want to write
                        else:
                            f.write(line)
                #.................................................end........................................................
                
                print(f"You Buy {self.Prodct} at the expense of Rs.{self.ExpenseAmount}/- ........and........ Your Current Account Balance= Rs.{self.BalanceAmount}/-")
                with open (f"{self.LedgerBookSerialNumber}.txt",'a') as f:
                    f.write(f"You Buy {self.Prodct} at the expense of Rs.{self.ExpenseAmount}/- ........and........ Your Current Account Balance= Rs.{self.BalanceAmount}\n\n")
                self.contine=int(input("For adding more expense please press Any number  and for discontinue press 0:- "))
                if self.contine == False:
                    break
        except FileNotFoundError:
                print("Ledger Book not found. Please enter a Ledger Book Serial number.")
        except ValueError:
                print("Invalid input. Please enter a valid amount.")
    def view_transaction(self):
        try:
            self.LedgerBookSerialNumber = input("Enter Ledger Book Serial Number:- ")
            with open(f"{self.LedgerBookSerialNumber}.txt",'r') as f:#read the file
                print(f.read())
        except FileNotFoundError:
                print("Ledger Book not found. Please enter a valid Ledger Book Serial number.")


Bank = Expenses()
Bank.your_choice()
