'''	
	@Author: Subhadeep Bhattacharjee
	@Date: 2021-11-19 15:00
	@Title : Quadratic equations roots
	
'''
import cmath
#we imported c math to perform complex operations as roots can be irrational

def calc_roots(a,b,c):
    """	
	Description:
	    This function helps us to find the roots of a quadratic equation
	Parameter:
	    Three numbers as the coefficients of the equation
	Return:
	    The two roots of the equation
	"""
    #The formula to finad the delta value
    delta = (b*b)-(4*a*c)
    root1 =(-b + cmath.sqrt(delta))/(2*a)
    root2= (-b - cmath.sqrt(delta))/(2*a)
    root1 = str(root1)
    root2 = str(root2)
    return ("The roots are: "+root1+ " and "+root2)

#For the eqn ax2 + bx + c
a= float(input("Please enter the coefficient of x2: "))
b= float(input("Please enter the coefficient of x: "))
c= float(input("Please enter the constant: "))

print(calc_roots(a,b,c))