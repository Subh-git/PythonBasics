'''	
	@Author: Subhadeep Bhattacharjee
	@Date: 2021-11-22 15:00
	@Title : This file contains all the detailed functions of the address book

'''
import re
import json

class AddressBookEntry:
    

    @staticmethod
    def open_validation():
        '''
        Description:
            This function is useful for checking and validating with the regex pattern
        Parameter:
            This opens the file handle to perform other operations.
        '''
        try:
            #file is the alias variable name where we are performing the read operation
            regex = []
            with open('C:/Users/subha/PythonBasics/OOPS/Address Book/JSONValidation.json', 'r') as file:
                regex = json.load(file)
                return regex

        except FileNotFoundError:
            print('Could Not open the file')

    @staticmethod
    def name_check():
        '''
        Description:
            This function is useful for checking and validating name with the regex pattern
        Parameter:
            This fethches the required regex and then checks with it
        '''
        regex = AddressBookEntry.open_validation()
        try:
            name = input("Please enter your name: ")
            if re.match(regex[0]['name'],name):
                return name
            else:
                print("Name should begin with capital letter")
        
        except ValueError:
            print("Invalid input")
        
    @staticmethod
    def mobile_check():
        '''
        Description:
            This function is useful for checking and validating mobile with the regex pattern
        Parameter:
            This fethches the required regex and then checks with it
        '''
        regex = AddressBookEntry.open_validation()
        try:
            mobile = input("Please enter your mobile number: ")
            if re.match(regex[0]['mobile'], mobile):
                return mobile
            else:
                print ("Mobile number should be of 10 digits")
        
        except ValueError:
            print("Invalid input")

    @staticmethod
    def email_check():
        '''
        Description:
            This function is useful for checking and validating email with the regex pattern
        Parameter:
            This fethches the required regex and then checks with it
        '''
        regex = AddressBookEntry.open_validation()
        try:
            email = input("Please enter your email: ")
            if re.match(regex[0]['email'], email):
                return email
            else:
                print ("Email format is incorrect")
        
        except ValueError:
            print("Invalid input")

    @staticmethod
    def address_check():
        '''
        Description:
            This function is useful for checking and validating address with the regex pattern
        Parameter:
            This fethches the required regex and then checks with it
        '''
        regex = AddressBookEntry.open_validation()
        try:
            address = input("Please enter your address: ")
            if re.match(regex[0]['address'], address):
                return address
            else:
                print ("Address should begin with capital letter")
        
        except ValueError:
            print("Invalid input")

    @staticmethod
    def zip_check():
        '''
        Description:
            This function is useful for checking and validating zip with the regex pattern
        Parameter:
            This fethches the required regex and then checks with it
        '''
        regex = AddressBookEntry.open_validation()
        try:
            zip = input("Please enter your zip: ")
            if re.match(regex[0]['zip'], zip):
                return zip
            else:
                print ("Zip should be 6 digit integer")
        
        except ValueError:
            print("Invalid input")

    @staticmethod
    def city_check():
        '''
        Description:
            This function is useful for checking and validating city with the regex pattern
        Parameter:
            This fethches the required regex and then checks with it
        '''
        regex = AddressBookEntry.open_validation()
        try:
            city = input("Please enter your city: ")
            if re.match(regex[0]['city'], city):
                return city
            else:
                print ("City should be alphabets only")
        
        except ValueError:
            print("Invalid input")

    @staticmethod
    def state_check():
        '''
        Description:
            This function is useful for checking and validating state with the regex pattern
        Parameter:
            This fethches the required regex and then checks with it
        '''
        regex = AddressBookEntry.open_validation()
        try:
            state = input("Please enter your state: ")
            if re.match(regex[0]['state'], state):
                return state
            else:
                print ("State should be alphabets only")
        
        except ValueError:
            print("Invalid input")
    



        

        
        
        
    
