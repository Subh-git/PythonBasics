'''	
	@Author: Subhadeep Bhattacharjee
	@Date: 2021-11-23 11:00
	@Title : This file stores the details about the CURD operation

'''

import json
from AddressBookEntry import AddressBookEntry


class AddressbookMethods:

    def __init__(self):
        self.address_list = []

    
    def save(self):
        '''
        Description:
            This method is writing or storing address book details from list into json file
        Parameter:
            It takes self as a parameter to get addressbook details stored inside list and
            using json dump it writes those details into the json file.
        '''
  
        try:
            #here the file is an alias for variable name
            # indent=2 symbolises the indentation to make it look better
            #w+ indicates the write and read, this overwrites the file operation
            with open('addressbook.json', 'w') as file:
                json.dump(self.address_list, file, indent=2)
                print("Json file modified")
        
        except Exception as e:
            print(e)

        finally:
            file.close()

    
    def open_json(self):
        '''
        Description:
            This method is used for opening and loading stored details from a json file.
        Parameter:
            It takes self as a parameter and load all the data from json file to a list.
        '''
        try:
            #file is the alias variable name where we are performing the read operation
            with open('addressbook.json', 'r') as file:
                self.address_list = json.load(file)

        except FileNotFoundError:
            print('Invalid file name')

    
    def add(self):
        '''
        Description:
            This function is used to add the details in a newly created dictionary
          Parameter:
            It has self as the parameter and append all details into the list
        '''
        #creating a new dictionary
        AddBook = {}
        name = AddressBookEntry.name_check()
        AddBook['name']=name
        mobile = AddressBookEntry.mobile_check()
        AddBook['mobile']=mobile
        email = AddressBookEntry.email_check()
        AddBook['email']=email
        address = AddressBookEntry.address_check()
        AddBook['address']=address
        zip = AddressBookEntry.zip_check()
        AddBook['zip']=zip
        city = AddressBookEntry.city_check()
        AddBook['city']=city
        state = AddressBookEntry.state_check()
        AddBook['state'] = state
        self.address_list.append(AddBook)
        self.save()

    def edit(self):
        '''
        Description:
            This function is used to edit the existing entry in json file
        Parameter:
            It takes self as the parameter and then edits the elemnet corresponding to their name
        '''
        try:
            self.open_json()
            if len(self.address_list) >=1:
                name = input("Enter the name of the user you want to edit: ")
                for i in range(len(self.address_list)):
                    if (self.address_list[i]['name']== name):
                        num = int(input("Choose what u want to update--- \n 1. All details 2. Partial details:  "))
                        if (num == 1):
                            AddBook = {}
                            name = AddressBookEntry.name_check()
                            AddBook['name']=name
                            mobile = AddressBookEntry.mobile_check()
                            AddBook['mobile']=mobile
                            email = AddressBookEntry.email_check()
                            AddBook['email']=email
                            address = AddressBookEntry.address_check()
                            AddBook['address']=address
                            zip = AddressBookEntry.zip_check()
                            AddBook['zip']=zip
                            city = AddressBookEntry.city_check()
                            AddBook['city']=city
                            state = AddressBookEntry.state_check()
                            AddBook['state'] = state
                            del self.address_list[i]
                            self.address_list.insert(i,AddBook)
                            self.save()

                        elif(num == 2):
                            choice = int(input("Select what you want to edit: \n 1. Name 2. Mobile 3. Email 4. Address 5. Zip 6. City 7. State:  "))
                            if (choice == 1):
                                name = AddressBookEntry.name_check()
                                self.address_list[i]['name'] = name
                                self.save()

                            elif (choice == 2):
                                mobile = AddressBookEntry.mobile_check()
                                self.address_list[i]['mobile'] = mobile
                                self.save()

                            elif (choice == 3):
                                email = AddressBookEntry.email_check()
                                self.address_list[i]['email'] = email
                                self.save()

                            elif (choice == 4):
                                address = AddressBookEntry.address_check()
                                self.address_list[i]['name'] = address
                                self.save()
                            
                            elif (choice == 5):
                                zip = AddressBookEntry.zip_check()
                                self.address_list[i]['zip'] = zip
                                self.save()
                            
                            elif (choice == 6):
                                city = AddressBookEntry.city_check()
                                self.address_list[i]['city'] = city
                                self.save()

                            elif (choice == 7):
                                state = AddressBookEntry.state_check()
                                self.address_list[i]['state'] = state
                                self.save()
                            
                            else:
                                print("Invalid selection")

            else:
                print("Ther are no entries")
        except ValueError:
            print("Invalid input")
        except Exception as e:
            print(e)

    
    def remove(self):
        '''
        Description:
            This method is used for deleting address book details from the json file.
        Parameter:
            It takes self as a parameter to get addressbook details stored inside list and
            delete the details and then save the json file.
        '''
        try:
            if len(self.address_list) >= 1:
                name = input("Enter your name: ")
                for i in range(len(self.address_list)):
                    if ((self.address_list[i]['name']) == name): 
                        print(" Data Removed Successfully ")
                        del self.address_list[i]
                        self.save()
            else:
                print("There is nothing to delete")
                    
        except Exception as e:
            print(e)


    def display(self):
        '''
        Description: 
            This method displays all the data in the addressbook list
        Parameter:
            This takes self as the parameter and therby displays all the elements one after the other

        '''
        try:
            if( len(self.address_list)>=1):
                for i in range(len(self.address_list)):
                    print("Name = ", self.address_list[i]['name'])
                    print("Mobile = ", self.address_list[i]['mobile'])
                    print("Email = ", self.address_list[i]['email'])
                    print("Address = ", self.address_list[i]['address'])
                    print("Zip = ", self.address_list[i]['zip'])
                    print("City = ", self.address_list[i]['city'])
                    print("State = ", self.address_list[i]['state'])
                    print("-------------------------------------------------")
            else:
                print("Currently empty")
        except Exception as e:
            print(e)



                                




        

    