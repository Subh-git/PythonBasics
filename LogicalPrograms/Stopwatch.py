'''	
	@Author: Subhadeep Bhattacharjee
	@Date: 2021-11-20 19:00
	@Title : Stopwatch simulator

'''
import time

def stop_watch():
    """	
	Description:
	    This function helps us to use a digital stopwatch in python program
	Parameter:
	    It has no parameter however it's internal message will prompt for input
	Return:
	    The the time elapsed in seconds
	"""
    
    try:
        while True:
            #Press Enter to start/stop the stopwatch
            start = input("Press Enter to start:")
            startTime = time.time()
            print("\n Stopwatch runnig.....")
            stop = input("\n Press Enter to stop:")
            endTime = time.time()
            timeElapsed = int(endTime - startTime)
            print("Time elapsed from Start to Stop is: ",timeElapsed, " Sec")
    
    except ValueError:
        print("Invalid input ")

stop_watch()





