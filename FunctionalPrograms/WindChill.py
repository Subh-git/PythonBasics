'''	
	@Author: Subhadeep Bhattacharjee
	@Date: 2021-11-19 19:00
	@Title : Wind Chill program
	
'''


def wind_chill(t,v):
    """	
	Description:
	    This function helps us to find the windchill
	Parameter:
	    Two floating point numbers representing temperature and wind speed
	Return:
	    The wind chill value
	"""
    d = (0.4275*t - 35.75)*(v**0.16)
    w = 35.74 + (0.6215*t) + d
    return w

temperature = float(input("Please enter your temperature in Fahrenheit: "))
speed = float(input("Please enter your wind speed in miles per hour: "))
print("The wind chill index in Fahreheit is: ",wind_chill(temperature,speed))