'''	
	@Author: subhadeep Bhattacharjee
	@Date: 2021-11-18 22:00
	@Title : To obtain the prime factors of a given number	
'''
num = int(input("Plese enter your number: "))

def prime_factors(n): 
    """	
	Description:
	    This function generates the prime factors of a given number
	Parameter:
	    The number whose factors are needed
	Return:
	    A list of prime factors
	"""
    i = 2
    factor = list()
    while (i * i <= n):
        if n % i:
            i += 1
        else:
            n = int(n / i)
            factor.append(i)
    if n > 1:
        factor.append(n)
    return factor

print(prime_factors(num))
