'''	
	@Author: Subhadeep Bhattacharjee
	@Date: 2021-11-22 18:00
	@Title : This file is the main entry file

'''

import json
from AddressValidation import AddressValidation

class AddressBookMain:

        def __init__(self):
            self.list = []

        def add(self):
            '''
        Description:
            This function is used to add the details in a newly created dictionary
          Parameter:
            It has self as the parameter and append all details into the list
        '''
            #initialising an empty dictionary
            addNew = dict()
            #calling the validating name method and appending it to the dictionary with name as the key
            name = AddressValidation.validate_name()
            addNew['name'] = name
            mobile = AddressValidation.validate_mobile()
            #mobile as the key with return from the validate address method
            addNew['mobile'] = mobile
            address = AddressValidation.validate_address()
            addNew['address'] = address
            #zip as the key
            zip = AddressValidation.validate_zip()
            addNew['zip'] = zip
            city = AddressValidation.validate_city()
            addNew['city'] = city
            state = AddressValidation.validate_state()
            addNew['state'] = state
            self.list.append(addNew)
            #self
            self.save()

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
                with open('addressbook.json', 'w+') as file:
                    json.dump(self.list, file, indent=2)
                    print("Entry added in json file")
        
            except Exception as e:
                print(e)

            finally:
                file.close()


        def open(self):
            '''
        Description:
             This method is used for opening and loading stored details from a json file.
        Parameter:
           It takes self as a parameter and load all the data from json file to a list.
        '''
            try:
                #file is the alias variable name where we are performing the read operation
                with open('addressbook.json', 'r') as file:
                    self.list = json.load(file)

            except FileNotFoundError:
                print('Invalid file name')


        def update(self):
            '''
            Description:
                This method is used for update addressbook details from the json file
            Parameter:
                It takes self as a parameter to get addressbook details stored inside list and
                update the details and save them into json file.            
            '''
            
            try:            
                flag = updateDetails = False
                if len(self.list) >= 1:
                    name = input("Enter your Name: ")
                    for i in range(len(self.list)):
                        if (self.list[i]['name'] == name):
                            flag = True
                            if flag:
                                option = int(
                                input(" Select any one : \n 1.Name \n 2. Mobile \n 3.Address \n 4.Zip \n 5. City \n 6. State"))

                                if option == 1:
                                    name = AddressValidation.validate_name()
                                    self.list[i]['name'] = name
                                    self.save()
                                    updateDetails = True

                                elif option == 2:
                                    mobile = AddressValidation.validate_number()
                                    self.list[i]['mobile'] = mobile
                                    self.save()
                                    updateDetails = True

                                elif option == 3:
                                    address = AddressValidation.validate_address()
                                    self.list[i]['address'] = address
                                    self.save()
                                    updateDetails = True

                                elif option == 4:
                                    zip = AddressValidation.validate_zip()
                                    self.list[i]['zip'] = zip
                                    self.save()
                                    updateDetails = True

                                elif option == 5:
                                    city = AddressValidation.validate_city()
                                    self.list[i]['city'] = city
                                    self.save()
                                    updateDetails = True

                                elif option == 6:
                                    state = AddressValidation.validate_state()
                                    self.list[i]['state'] = state
                                    self.save()
                                    updateDetails = True

                                else:
                                    print("Invalid Option")
                                    updateDetails = False
                                    self.update()
                else:
                    print("There are cuurently no entries")

            except ValueError:
                print("Invlaid input")
                updateDetails = False
                self.update()

            except Exception as e:
                print(e)
                self.update()

        def remove(self):
            '''
            Description:
                This method is used for deleting address book details from the json file.
            Parameter:
                It takes self as a parameter to get addressbook details stored inside list and
                delete the details and then save the json file.
            '''
            try:
                if len(self.list) >= 1:
                    name = input("Enter your name: ")
                    for i in range(len(self.list)):
                        if ((self.list[i]['name']) == name): 
                            print(" Data Removed Successfully ")
                            del self.list[i]
                            self.save
                else:
                    print("There is nothing to delete")
                    
            except Exception as e:
                print(e)

        def display(self):
            '''
            Description:
                This method is used for displaying addressbook details from a json file
            Parameter:
                It takes self as a parameter to get addressbook details stored inside list and
                display all the stored details.

            '''
            if len(self.list) >= 1:
                for i in range(len(self.list)):
                    print(self.list[i]['name'])
                    print(self.list[i]['mobile'])
                    print(self.list[i]['address'])
                    print(self.list[i]['zip'])
                    print(self.list[i]['city'])
                    print(self.list[i]['state'])
            else:
                try:
                    print("Currently empty.")
                    choice = input("Do you want to add another record? y/n ")
                    if (choice.upper() == "Y"):
                        self.add()
                    elif( choice.upper() == "N"):
                        exit()
                    else:
                        print("Please press y or n")
                except ValueError as e:
                    print(e)


if __name__ == '__main__':
    try:
        while True:
            address = AddressBookMain()
            op = int(input("Press \n 1. Add New Address Book 2. To Existing Book 3. To Quit \n"))
            if op == 1:
                choice = int(input(' Select the option you want to choose:- \n 1. To Add new contact \n 2. To Delete\n 3. To Update address book\n'
                                   ' 4. To Print Book \n' ' 5. To Quit \n '))  # Asks user for input
                if choice == 1:
                    address.add()

                elif choice == 2:
                    address.remove()
                   
                elif choice == 3:
                    address.update()
                   
                elif choice == 4:
                    address.open()
                    address.display()
                   
                elif choice == 5:
                  
                    exit()
            elif op == 2:
                address.open() # opening the file
                address.add()
            elif op == 3:
                exit()
    except KeyboardInterrupt:
        print("\nForce Quit ")
    except ValueError:
        print("Invalid Option")      

    
    
    
