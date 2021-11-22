'''	
	@Author: Subhadeep Bhattacharjee
	@Date: 2021-11-22 15:00
	@Title : This file contains all the detailed functions of the address book

'''
import re

class AddressValidation:
    
   
    def validate_name():
        '''
        Description:
            This function implemented for validating name using regex.
          Parameter:
            Empty, but needs input
        Return:
            This function returns valid name if it matches to the proper standard
        '''

        try:
            name = input("Enter your name :")
            if re.match("^[A-Z]{1}[a-z]*$", name):
                return name
            else:
                print("Name should be alphabets starting with Capital letter")

        except ValueError:
            print("Invalid input")

    def validate_mobile():
        '''
        Description:
            This function implemented for validating mobile number using regex.
        Parameter:
            Empty, but needs input
        Return:
            This function returns a valid mobile number if it matches to the proper standard
        ''' 
        try:
            mobile = input("Enter your mobile number :")
            if re.match("^[7-9]{1}[0-9]*$", mobile):
                return mobile
            else:
                print("mobile number should be numeric")

        except ValueError:
            print("Invalid input")


    def validate_address():
        '''
        Description:
            This function implemented for validating address using regex.
        Parameter:
            Empty, but needs input
        Return:
            This function returns a valid address if it matches to the proper standard
        '''
        try:
            address = input("Enter your Address : ")
            if re.match("^[A-Z]{1}[a-z]*$", address):
                return address
            else:
                print("Address should be in alphabets starting with Capital letter")

        except ValueError:
            print("Invalid input")

    def validate_zip():
        '''
        Description:
            This function implemented for validating zipcode using regex.
         Parameter:
            Empty, but needs input
        Return:
            This function returns a valid zipcode if it matches to the proper standard
        '''
        try:
            zip = input("Enter your zip :")
            if re.match("^[1-9]{1}[0-9]{5}$", zip):
                return zip
            else:
                print("zip should be numeric and 6 numbers")

        except ValueError:
            print("Invalid input")

    def validate_city():
        '''
        Description:
            This function implemented for validating city using regex.
        Parameter:
            Empty, but needs input
        Return:
            this function returns a valid city if it matches to the proper standard
        '''
        try:
            city = input("Enter your city :")
            if re.match("^[A-Za-z]*$", city):
                return city
            else:
                print("City should be alphabets")

        except ValueError:
            print("Invalid input")

    def validate_state():
        '''
        Description:
            This function implemented for validating state using regex.
        Parameter:
            Empty, but needs input
        Return:
            this function returns a valid state if it matches to the proper standard
        '''
        try:
            state = input("Enter your state :" )
            if re.match("^[A-Za-z]*$", state):
                return state
            else:
                print("State should be in alphabets")

        except ValueError:
            print("Invalid input")