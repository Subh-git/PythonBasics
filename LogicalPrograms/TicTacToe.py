'''	
	@Author: Subhadeep Bhattacharjee
	@Date: 2021-11-20 21:45
	@Title : Tic Tac Toe game 

'''
#importing random class as we need it to 
import random

#10 spaced empty list 
board = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']

running = 0
player = 1
win=1
draw=-1
game = running


def draw_board():
    """
    Description:
        This Function prints the Game Board
    """
    print(" %c | %c | %c " % (board[1],board[2],board[3]))    
    print("___|___|___")    
    print(" %c | %c | %c " % (board[4],board[5],board[6]))    
    print("___|___|___")    
    print(" %c | %c | %c " % (board[7],board[8],board[9]))    
    print("   |   |   ")

def check_position(x):
    """
    Description:
        This Function checks position is empty or not
    Return:
        This function returns bool value of true or false
    """
    if(board[x] == ' '):
        return True
    else:
        return False

def check_win():
    """
    Description:
        This Function Checks player has won or not
    """
    #global keyword is used to asssign the variable which can be used the function's scope
    global game
    
    # Horizontal Winning condition that checks the board index marked similarity
    if(board[1] == board[2] and board[2] == board[3] and board[1] != ' '):
        game = win
    elif(board[4] == board[5] and board[5] == board[6] and board[4] != ' '):
        game = win
    elif(board[7] == board[8] and board[8] == board[9] and board[7] != ' '):
        game = win
    
    # Vertical Winning Condition
    elif(board[1] == board[4] and board[4] == board[7] and board[1] != ' '):
        game = win
    elif(board[2] == board[5] and board[5] == board[8] and board[2] != ' '):
        game = win
    elif(board[3] == board[6] and board[6] == board[9] and board[3] != ' '):
        game = win

    # Diagonal Winning Condition
    elif(board[1] == board[5] and board[5] == board[9] and board[5] != ' '):
        game = win
    elif(board[3] == board[5] and board[5] == board[7] and board[5] != ' '):
        game = win

    # Match Tie or Draw Condition 
    elif(board [1]!= ' ' and board[2] != ' ' and board[3] != ' '
        and board[4] != ' ' and board[5] != ' ' and board[6] != ' ' 
        and board[7] != ' ' and board[8] != ' ' and board[9] != ' '):
        game = draw
    else:
        game = running

print("Let's begin the game of Tic Tac Toe")
print("Computer takes [X] and Player takes [O] \n")
while(game == running):
    draw_board()
    try:
        if(player % 2 != 0):
            print("Computer's Chance \n")
            mark = 'X'
            choice = random.randint(1,9)
            if(check_position(choice)):
                board[choice] = mark
                player += 1
                check_win()

        else:
            print("Player's chance \n")
            mark = 'O'
            choice = int(input("Enter the position between [1-9] where you want to mark : "))    
            if(check_position(choice)):
                board[choice] = mark
                player += 1
                check_win()
            else:
                print("Occupied! Select another.")
    
    except ValueError:
        print("Invalid input")

draw_board()
if(game == draw):
    print("Game Draw")
elif(game == win):
    player-=1
    if(player % 2 != 0):
        print("Computer Won!")
    else:
        print("Player Won!")




        