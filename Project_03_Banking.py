#Programm for Banking(Open account,Deposit,Withdraw,View Transaction History)
class Banking:
    
    
    def __init__(self):
        self.AccountHolderName = ""
        self.AccountNumber = ""
        self.Capital = 0
        self.DepositingAmount = 0
        self.WithdrawAmount = 0
        self.BalanceAmount = 0
        self.Mobile = ""
        self.choice = 0
        self.CapitalChecking = 0
    
    
    def your_choice(self):
        # while True:
            try:

                self.choice = 0
                print("")
                self.choice = int(input("1)Open a new Account\n\n2)Deposit\n\n3)withdraw\n\n4)View Transaction History\n\nenter your choice:- "))
                if   self.choice == 1:
                     self.account_opening()
                elif self.choice == 2:
                     self.depositing()
                elif self.choice == 3:
                     self.withdraw()
                elif self.choice == 4:
                     self.view_transaction()
                else:
                    print("You enterd wrong choice please enter any of this choice \n1)Open a new Account\n2)Deposit\n3)withdraw\n4)View Transaction History")
            except ValueError:
                print("Invalid input Please enter integer number only")
    
    def account_opening(self):
        try:
            self.AccountHolderName = input("Enter your full Name:- ")
            self.Mobile = input("enter your mobile number:- ")
            self.AccountNumber = self.AccountHolderName+self.Mobile
            while self.CapitalChecking <= 499:
                self.CapitalChecking = int(input("enter the capital Amount for opening the Account(Minimum Deposit Amount is 500):- "))
                if self.CapitalChecking <= 499:
                    print("Sorry you need minimum Rs.500/- for Account opening")


            self.Capital=self.CapitalChecking
            self.BalanceAmount = self.Capital
            print(f"Welcome {self.AccountHolderName} You opened an Account Successfuly with Capital Amount of Rs.{self.Capital}/-. \nPlease note {self.AccountNumber} is your Account number")
            with open(f"{self.AccountNumber}.txt",'w') as f:
                f.write(f"Welcome {self.AccountHolderName} You opened an Account Successfuly with Capital Amount of Rs.{self.Capital}/-. \nAccount number:- {self.AccountNumber}\nBalance= Rs.{self.BalanceAmount}\n")
        except ValueError:
            print("Invalid input please enter An integer")
    
    def depositing(self):
        try:
            self.AccountNumber = input("Enter Account Number:- ")
            self.DepositingAmount = int(input("Enter the Depositing amount:- "))
        
            #programm for fetching Balance
            with open(f"{self.AccountNumber}.txt", 'r') as f:
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
            #..........end......................
        
            self.BalanceAmount = self.DepositingAmount + self.BalanceAmount
       
            #programm for updating balance for fetching
            with open(f"{self.AccountNumber}.txt", 'r') as f:
                lines = f.readlines()

            with open(f"{self.AccountNumber}.txt", 'w') as f:
                for line in lines:
                    if line.startswith('Balance= Rs.'):
                        f.write(f'Balance= Rs.{self.BalanceAmount}\n')  # Replace with the new value you want to write
                    else:
                        f.write(line)
            #..........end...............................................................................................
        
            print(f"You Deposited Rs.{self.DepositingAmount}/- ......and........ Your Current Account Balance= Rs.{self.BalanceAmount}/-\n\n")
            with open (f"{self.AccountNumber}.txt",'a') as f:
                f.write(f"You Deposited Rs.{self.DepositingAmount}/- ......and........ Your Current Account Balance= Rs.{self.BalanceAmount}\n\n")
        except FileNotFoundError:
            print("Account not found. Please enter a valid account number.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
    
    def withdraw(self):
        try:
            self.AccountNumber=input("Enter Account Number:- ")
            self.WithdrawAmount=int(input("Enter the Withdrawing Amount:- "))
            
            #programm for fetching Balance
            with open(f"{self.AccountNumber}.txt", 'r') as f:
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
            
            self.BalanceAmount=self.BalanceAmount-self.WithdrawAmount
        
            #programm for updating balance for fetching
            with open(f"{self.AccountNumber}.txt", 'r') as f:
                lines = f.readlines()

            with open(f"{self.AccountNumber}.txt", 'w') as f:
                for line in lines:
                    if line.startswith('Balance= Rs.'):
                        f.write(f'Balance= Rs.{self.BalanceAmount}\n')  # Replace with the new value you want to write
                    else:
                        f.write(line)
            #.................................................end........................................................
            
            print(f"You withdraw Rs.{self.WithdrawAmount}/- ........and........ Your Current Account Balance= Rs.{self.BalanceAmount}/-")
            with open (f"{self.AccountNumber}.txt",'a') as f:
                f.write(f"You withdraw Rs.{self.WithdrawAmount}/- ........and........ Your Current Account Balance= Rs.{self.BalanceAmount}\n\n")
   
        except FileNotFoundError:
                print("Account not found. Please enter a valid account number.")
        except ValueError:
                print("Invalid input. Please enter a valid amount.")
    def view_transaction(self):
        try:
            self.AccountNumber = input("Enter Account Number:- ")
            with open(f"{self.AccountNumber}.txt",'r') as f:#read the file
                print(f.read())
        except FileNotFoundError:
                print("Account not found. Please enter a valid account number.")


Bank = Banking()
Bank.your_choice()