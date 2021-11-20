'''	
	@Author: Subhadeep Bhattacharjee
	@Date: 2021-11-20 18:00
	@Title : Coupon number generator

'''
#importing the random class
import random  

def dis_coupons():
    """	
	Description:
	    This function lets us create N distinct coupon numbers and return the number of total number of random numbers required
	Parameter:
	    No parameter is requied
	Return:
        The integer value which equals to the total random numbers generated
    """
    #empty list      
    coupon = []
    count=0         #counter to count the total number of random numbers generated in the process 
    try:
        num=int(input("Enter The Number Of Coupons You Want To Generate: "))
        #The while loops compares the size of the list with the number of coupons we want
        while len(coupon)< num:
            coupon_number = random.randint(10,100)              #creating double digit coupons
            count = count+1
            if coupon_number not in coupon:
                coupon.append(coupon_number)          #adding the distinct random number gnerated to list 
            
            else:
                pass
        count = str(count)
        return ("Total random numbers generated to obtain distinct coupons are: "+count)

    except Exception as err:
        print("Not A Valid Number",err)

print(dis_coupons()) 