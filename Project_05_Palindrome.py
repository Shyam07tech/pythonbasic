class Palindrome:
    def __init__(self):
        self.Number=0
        self.ForCompare1=0
        self.ForCompare2=0
        self.TempStore=0
    def input(self):
        while True:
            try:
                self.Number=int(input("enter the input:-"))
                break
            except ValueError:
                print("ERROR!!!...Only enter integer value")
        self.ForCompare1=self.Number
        while self.Number!=0:
            self.TempStore=self.Number%10
            self.ForCompare2=self.ForCompare2*10+self.TempStore
            self.Number=self.Number//10
            if self.Number==0:
                break
            
        
    def display(self):
        self.input()
        if self.ForCompare1 !=0:
            if self.ForCompare1==self.ForCompare2:
                print(f"Given Number {self.ForCompare1} is palindrome")
            else:
                print(f"given Number {self.ForCompare1} is not palindrome")
Pali=Palindrome()
Pali.display()

