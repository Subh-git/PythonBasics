'''	
	@Author: subhadeep Bhattacharjee
	@Date: 2021-11-18 19:00
	@Title : Mimicking the coin flip simulator
	
'''

from random import random

def flip_coin (n):
    """	
	Description:
	    This function works as a coin flip simulator
	Parameter:
	    A positive integer as the number of times the coin must be flipped
	Return:
	    Percentage of heads and tails
	"""
    count = 0 
    tails = 0
    heads = 0
    while(count < n):
        flip = random()
        if (flip < 0.5):
            tails= tails+1
        else:
            heads = heads+1
        count= count+1
    heads_percent = str((heads/n)*100)
    tails_percent = str((tails/n)*100)
    return ("The percentage of heads is "+heads_percent+" and the number of tails is "+tails_percent)

print(flip_coin(56))

