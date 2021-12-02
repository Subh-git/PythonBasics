'''	
	@Author: Subhadeep Bhattacharjee
	@Date: 2021-12-02 22:45
	@Title : This file is the main inventory manager file.

'''
import json
from Inventory import InventoryManager

if __name__ == '__main__':
    try:
        inventory_factory = InventoryManager()

        while True:
            option = int(input('Please select the suitable option. \n 1. Create new inventory 2. Modify Existing Inventory 3. View Inventory  4. Delete Inventory 5. Exit  '))
            
            if option == 1:
                inventory_factory.create_inventory()

            elif option ==2:
                inventory_factory.edit_inventory()

            elif option ==3:
                inventory_factory.view()

            elif option ==4:
                inventory_factory.remove()

            elif option ==5:
                exit()
            else:
                print("Invalid option!")

    except ValueError:
        print("Invalid input")
    except Exception as e:
        print(e)


