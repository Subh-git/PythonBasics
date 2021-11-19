'''	
	@Author: Subhadeep Bhattacharjee
	@Date: 2021-11-19 19:40
	@Title : Sum of Triplets equals zero
	
'''

def find_triplets(arr,n):
    """	
	Description:
	    This function helps us identify the triplets whoose sum adds upto zero
	Parameter:
	    A list with the values and the lenght of that list
	Return:
	    The triplet combinations and the total number of distinct triplets
	"""
    found = False
    count = 0
    #the loop iterates upto the 3rd last element
    for i in range(0, n-2):
        #the loop iterates upto the 2nd last element               
        for j in range(i+1, n-1):
            #finally iterating upto the last element
            for k in range(j+1, n):
                if (arr[i] + arr[j] + arr[k] == 0):
                    print(arr[i], arr[j], arr[k])
                    count= count+1
                    found = True                
    
    # If no triplet with 0 sum
    if (found == False):
        print(" Triplets do not exist ")
    return count

num = int(input("Enter how many values: "))
n=1
arr = []
while(n<=num):
    n1 = str(n)
    val = int(input("Please enter the "+n1+" element: "))
    arr.append(val)
    n= n+1
print(find_triplets(arr,num))
