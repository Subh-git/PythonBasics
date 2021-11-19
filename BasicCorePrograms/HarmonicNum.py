'''	
	@Author: Subhadeep Bhattacharjee
	@Date: 2021-11-18 21:30
	@Title : To print the Harmonic number
	
'''
num = int(input("Please enter the number N upto whose harmonics are required :"))
count = 1
harmonic = 0
while(count <= num):
    harmonic = harmonic + (1/count)
    count = count+1
print(harmonic)