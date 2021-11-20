'''	
	@Author: Subhadeep Bhattacharjee
	@Date: 2021-11-20 20:00
	@Title : To Simulate a Gambling Game

'''
#importing the random class to take a random observation
import random
    
def gambling():
    """
    Description:
	    This function creates an automatic gambling experience
	Parameter:
	    No parameter to pass. Internally ask for inputs for stake,goal and max bets
	Return:
        The win/loose percentage, no.of times won/lost and no.of bets made
    """
    try:
        stake=int(input("Enter the stake amount: "))
        goal=int(input("Enter the amount you want to win: "))
        bet_max=int(input("Enter the maximum number of bets u can make: "))
    
    except ValueError:
        print("Invalid input")

    no_of_win=0
    no_of_loss=0
    no_of_bets=0

    #the while condition checks if the stake is between 0 or goal and whether the bets are less than max bets
    while(stake >= 0 and stake <= goal and no_of_bets < bet_max):
        no_of_bets+=1
        gambler_choice = random.randint(0, 1)  #generates a random number 0 or 1 to give a 50-50 chance
        
        if gambler_choice==0:   #if the random number generated is 0
            no_of_win+=1
            stake=stake+1 
        else:
            no_of_loss+=1
            stake=stake-1

    print("Money in hand--",stake)
    print("Number of times won",no_of_win)
    print("Num of times lost ", no_of_loss)
    print("Percentage of win", (no_of_win/bet_max)*100) 
    print("Percentage of loss", (no_of_loss/bet_max)*100)
    print("Number of bets made", no_of_bets) 
    
gambling()        