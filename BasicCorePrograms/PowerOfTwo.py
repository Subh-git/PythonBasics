'''	
	@Author: subhadeep Bhattacharjee
	@Date: 2021-11-18 21:00
	@Title : To print the power of two
	
'''
num = int(input("Please enter the the degree of 2's table: "))
count = 1
x = 2
while(count <= num):
    power = pow(2,count)
    count= count+1
    print(power)
    