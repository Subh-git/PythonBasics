'''	
	@Author: Subhadeep Bhattacharjee
	@Date: 2021-11-19 22:00
	@Title : Matrix or 2D array insertion
	
'''

def matrix(r,c):
    """	
	Description:
	    This function lets us enter and print 2D array
	Parameter:
	    Two integers describing number of rows and columns respectively
	Return:
        The 2D array matrix
    """
    mat = []  
    for i in range(r):
        a=[]
        for j in range(c):
            #changed the i and j values to string to let the user have clarity while inserting 
            i_str = str(i)
            j_str = str(j) 
            a.append(int(input("Please enter the "+i_str+ j_str+"th element")))
        mat.append(a)
   
    #for printing the matrix
    for i in range(r):
        for j in range(c):
            print(mat[i][j], end = " ")
        print()

#to take user inputs for the number of rows and cloumns            
row = int(input("Enter the number of rows: "))
col = int(input("Enter the number of columns: "))
matrix(row,col)


