'''	
	@Author: subhadeep Bhattacharjee
	@Date: 2021-11-18 20:00
	@Title : To check the input year is leap year or not	
'''

year = input("Please enter your year: ")
while(len(year) != 4):
    print("The entered year format is wrong, enter in YYYY.")
    year = input("Please enter the correct year: ")

year = int(year)
if ( (year % 4 == 0) and (year % 100 != 0) or (year % 400 ==0)):
    print("The year " ,year, " is a leap year")
else:
    print("The year ",year," is not a leap year")



    
