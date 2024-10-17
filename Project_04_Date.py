# Reformat Date

# Given a date string in the form Day Month Year, where:

# Day is in the set {"1st", "2nd", "3rd", "4th", ..., "30th", "31st"}.
# Month is in the set {"Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"}.
# Year is in the range [1900, 2100].
# Convert the date string to the format YYYY-MM-DD, where:

# YYYY denotes the 4 digit year.
# MM denotes the 2 digit month.
# DD denotes the 2 digit day.
 

# Example 1:

# Input: date = "20th Oct 2052"
# Output: "2052-10-20"
# Example 2:

# Input: date = "6th Jun 1933"
# Output: "1933-06-06"
# Example 3:

# Input: date = "26th May 1960"
# Output: "1960-05-26"
class ReformDate():
     def __init__(self):
          self.date_string = None
          self.date = None
          self.month = None
          self.year = None
          self.dates = None
          self.months = None
          self.old_monthlist = None
          self.new_monthlist = None
     def splited(self):  
          while True:
               try: 
                    self.date_string = input("Enter the Date in the format of DD MM YYYY(example:- 25th Jan 2000) :- ")
                    self.date,self.month,self.year = self.date_string.split()
                    break
               except ValueError:
                    print("Enter correct Date format(example:- 25th Jan 2000)")
               
     
     def Dated(self):
          try:
               self.date = self.date
               self.Old_datelist = ['1st','2nd','3rd','4th','5th','6th','7th','8th','9th','10th','11th','12th','13th','14th','15th','16th','17th','18th','19th','20th','21st','22nd','23rd','24th','25th','26th','27th','28th','29th','30th','31st']
               self.New_datelist = ['01','02','03','04','05','06','07','08','09',10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31]

               for i in range(len(self.Old_datelist)):
                    if self.Old_datelist[i] == self.date:
                         self.dates=self.Old_datelist[i]
                         for j in range(len(self.New_datelist)):
                              if i == j:
                                   return self.New_datelist[j]
               raise ValueError("Invalid date")
          except ValueError as e:
            print(f"Error: {e}")
     def Monthed(self):
          try:
               self.month = self.month
               self.old_monthlist = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'] 
               self.new_monthlist = ['01','02','03','04','05','06','07','08','09',10,11,12]          
          
               for i in range(len(self.old_monthlist)):
                    if self.old_monthlist[i] == self.month:
                         self.dates = self.old_monthlist[i]
                         for j in range(len(self.new_monthlist)):
                              if i == j:
                                   return self.new_monthlist[j]
               raise ValueError("Invalid month")
          except ValueError as e:
            print(f"Error: {e}")
            
     def Date_call(self):
          # self.splited()
          self.reformat_month=self.Monthed()
          self.reformat_date=self.Dated()

          if self.reformat_month != None and self.reformat_date != None:
               print(f"Before Reformat:- {self.date_string}")
               print(f'After Reformat:- {self.year}-{self.reformat_month}-{self.reformat_date}')
          else:
               print("Write date like this 25th or 1st etc.. and month must start with capital letter eg:-Mar or Jan etc... ")
          


          
          
          
All=ReformDate()
All.splited()
All.Date_call()

