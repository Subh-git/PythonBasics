'''	
	@Author: subhadeep Bhattacharjee
	@Date: 2021-11-18 20:00
	@Title : To check the input year is leap year or not	
'''

year = int(input("Please enter your year: "))
while(year >= 9999 or year <= 1000):
    print("The entered year format is wrong, enter in YYYY.")
    year = int(input("Please enter the correct year: "))

if ( (year % 4 == 0) and (year % 100 != 0) or (year % 400 ==0)):
    print("The year " ,year, " is a leap year")
else:
    print("The year ",year," is not a leap year")



    
