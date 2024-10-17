#Programm of HangmanGame Movie guessing
class HangMan:
    
    def __init__(self):
        self.set_movie = ""
        self.count = 0
        self.movie_name = ""
    
    def Setup(self):
        while True:
                try:
                    self.set_movie = input("Enter Movie Name for Player Guessing:-")
                    self.movie_name = list(self.set_movie)
                    if not self.set_movie.isupper():
                        print("The Name is not entirely in uppercase.")
                    else:
                        break
                except ValueError:
                    print("Only CAPITAL letters")
    
    def Hiding(self):
        self.guessed_letters = ['_'] * len(self.movie_name)
        print(' '.join(self.guessed_letters))#join() is a string methord actually convert gussedletters elements to string 
        print('\n\n')
    
    def Guess(self):
        while self.count != 8:
            while True:
                try:
                    self.Player_guess = input("Enter guessed letter (only one letter at a time):- ")
                    if not self.Player_guess.isupper():
                        print("The Letter is not in UPPERCASE.")
                    else:
                        if len(self.Player_guess) != 1:
                            print("ONLY ONE LETTER AT A TIME")
                        else:
                            break

                except ValueError:
                    print("Only CAPITAL letter")
            for i in range(len(self.movie_name)):
                if self.Player_guess == self.movie_name[i]:
                    self.guessed_letters[i] = self.Player_guess
            print(' '.join(self.guessed_letters))
            if self.Player_guess not in self.movie_name:
                self.count = self.count + 1
                print("Incorrect! You have", 8 - self.count, "chances left.")

            if '_' not in self.guessed_letters:
                print("Congratulations! You won!")
                break
            elif self.count == 8:
                print("Game over! The movie name was", self.set_movie)
                break
    
    def Game_play(self):
        self.Setup()
        self.Hiding()
        self.Guess()

Game = HangMan()
Game.Game_play()
        