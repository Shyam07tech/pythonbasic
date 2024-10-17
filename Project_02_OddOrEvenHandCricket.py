import random

class OddOrEvenCricket:
    def __init__(self):
        self.even_count = 0
        self.odd_count = 0
        self.round_count = 0
        self.player1 = 0
        self.player2 = 0
    
    def player_odd_even_choice(self):
        while True:        
                try:           
                    self.player_one = int(input("Player, if your choice is odd then Enter 1 else choice is even, enter 2: "))
                    self.player_two = int(input("Player, if your choice is odd then Enter 1 else choice is even, enter 2: "))
                    if (self.player_one not in [1,2] and (self.player_two not in [1,2])):
                        print(" !!!!Invalid input!!!!!  Please check Your Choice.... for odd press 1 and for even press 2")
                    else:
                        break
                except ValueError:
                        print("Invalid input! Please enter a valid number.")    

    
    def guessing(self):
        while self.round_count != 6:
            self.player1 = random.randint(1, 6)
            self.player2 = random.randint(1, 6)
            print(f'First Player choice: {self.player1} \n\nSecond Player Choice: {self.player2}\n')
            total = self.player1 + self.player2
            print(total)
            
            if total % 2 == 0:
                self.even_count = self.even_count + 1
            else:
                self.odd_count = self.odd_count + 1
            
            self.round_count = self.round_count + 1
    
    def Check(self):
        if self.player_one == 2 and self.player_two == 1:
            if self.even_count > self.odd_count:
                print(f"First player won.... player one scored {self.even_count} player two scored {self.odd_count}")
            elif self.even_count == self.odd_count:
                print(f"It's a Tie Match.... player one scored {self.even_count} player two scored {self.odd_count}")
            else:
                print(f"Second player won.... player one scored {self.even_count} player two scored {self.odd_count}")
        else:
            if self.even_count < self.odd_count:
                print(f"First player won.... player one scored {self.even_count} player two scored {self.odd_count}")
            elif self.even_count == self.odd_count:
                print(f"It's a Tie Match.... player one scored {self.even_count} player two scored {self.odd_count}")
            else:
                print(f"Second player won.... player one scored {self.even_count} player two scored {self.odd_count}")
    
    def GamePlay(self):
        self.player_odd_even_choice()
        self.guessing()
        self.Check()

Game=OddOrEvenCricket()
Game.GamePlay()