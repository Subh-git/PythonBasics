'''	
	@Author: Subhadeep Bhattacharjee
	@Date: 2021-11-19 14:35
	@Title : Distance of a point from origin
	
'''

def calc_distance(x, y):
    """	
	Description:
	    This function enables us to calculate the distance of a point from origin
	Parameter:
	    Two integer values as the coordinates of the point
	Return:
	    The distance of the point from origin(0,0)
	"""
    #the formula of calculating distance from origin is dist= sqrt((x1-0)**2 + (y1-0)**2)
    dist = ((x*x)+(y*y))**0.5
    return dist

x1= int(input("Please enter x coordinate: "))
y1= int(input("Please enter y coordinate: "))

result = calc_distance(x1,y1)
print("The distance from the origin is: ",result)