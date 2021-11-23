'''	
	@Author: Subhadeep Bhattacharjee
	@Date: 2021-11-23 13:00
	@Title : This is the main executable file

'''

import json
from AddressBookEntry import AddressBookEntry
from AddressBookMethods import AddressbookMethods


if __name__ == '__main__':
    try:

        addressbook = AddressbookMethods()
        while True:
            num = int(input("Please choose from the following options: \n 1. Create/Modify Address Book 2. Exit:  "))
            if num == 1:
                option = int(input("Select the operation you want to perform. \n 1. Add New Contact 2. Edit Existing Contact 3. Delete Existing Contact 4. Display Conatct---------  "))
                if option == 1:
                    addressbook.add()
                elif option ==2:
                    addressbook.edit()
                elif option == 3:
                    addressbook.open_json()
                    addressbook.remove()
                elif option == 4:
                    addressbook.open_json()
                    addressbook.display()
                else:
                    print("Invalid selction")
            elif( num == 2):
                exit()
            else:
                print("Select 1 or 2")
    
    except ValueError:
        print("Invlaid input type")
    except Exception as e:
        print(e) 

        
