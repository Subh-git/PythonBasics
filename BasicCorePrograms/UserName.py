'''	
	@Author: subhadeep Bhattacharjee
	@Date: 2021-11-18 18:00
	@Title : Taking user name as input and showcasing a greeting
	
'''
import re
# importing regex to use regular exp

name = input("Please enter your name: ")
str = "[a-zA-Z]{3,}"

if(re.match(str,name)):
	print("Hello " +name+",How are you?")
else:
	print("Invalid name")

