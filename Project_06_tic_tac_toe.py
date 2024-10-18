#Programm for tic tac toe Game (basic)
import random
board=[' ']*10
computer='X'
human='O'
def display_board(board):
    print(f" {board[1]} | {board[2]} | {board[3]}")
    print(f"___|___|___")
    print(f" {board[4]} | {board[5]} | {board[6]}")
    print(f"___|___|___")
    print(f" {board[7]} | {board[8]} | {board[9]}")
    print(f"   |   |  ")
    print()

def check_win():
    #vertical win movements
    if board[1] == board[4] == board[7] and board[1] != ' ':
        return True
    elif board[2] == board[5] == board[8] and board[2] != ' ':
        return True
    elif board[3] == board[6] == board[9] and board[3] != ' ':
        return True
    #Horizontal win Movement
    elif board[1] == board[2] == board[3] and board[1] != ' ':
        return True
    elif board[4] == board[5] == board[6] and board[4] != ' ':
        return True
    elif board[7] == board[8] == board[9] and board[7] != ' ':
        return True
    #Diagonal win movements
    elif board[1] == board[5] == board[9] and board[1] != ' ':
        return True
    elif board[7] == board[5] == board[3] and board[7] != ' ':
        return True
    else:
        return False

def is_avaliable(pos):
    return True if board[pos] == ' ' else False

def check_draw():
    if board.count(' ') < 2:
        return True
    else:
        return False
def insert(letter,pos):
    if is_avaliable(pos):
        board[pos] = letter
        if check_win():
            display_board(board)
            if letter == 'X':
                print("Game Over...! Computer Won")
                exit()
            else:
                print("Congratulation...! You Won")
                exit()
        if check_draw():
            display_board(board)
            print("The Game is Finished As tie")
            exit()
        
    else:
        if letter == 'O':
            pos = int(input("Not free please reenter position:- "))
        else:
            pos = random.randint(1,9)
        insert(letter,pos)

                

def computer_mov(letter):
    pos=random.randint(1,9)
    insert(letter,pos)

def human_mov(letter):
    while True:
        try:
            pos = int(input("Player, choose your position (1-9): "))
            if pos < 1 or pos > 9:
                raise ValueError("Position out of range. Please choose between 1 and 9.")
            insert(letter, pos)
            break
        except ValueError as e:
            print(f"Invalid input: {e}. Please enter a valid position.")


#Main loop
while True:
    display_board(board)
    human_mov(human)
    if check_win() or check_draw():
        break
    display_board(board)
    computer_mov(computer)
    if check_win() or check_draw():
        break
    
