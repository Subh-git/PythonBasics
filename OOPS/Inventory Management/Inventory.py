'''	
	@Author: Subhadeep Bhattacharjee
	@Date: 2021-12-02 18:45
	@Title : This file contains the methods of inventory management.

'''
import json

class InventoryManager:


    def __init__(self):
        self.inventory_list = []


    def save(self):
        '''
        Description:
            This method is writing or storing the inventorty details into the json file
        Parameter:
            It takes self as a parameter to refer to the list.
        '''
        try:
            #here the file is an alias for variable name
            # indent=2 symbolises the indentation to make it look better
            #w+ indicates the write and read, this overwrites the file operation

            with open('C:/Users/subha/PythonBasics/OOPS/Inventory Management/Inventory.json', 'w') as file:
                json.dump(self.inventory_list, file, indent=2)
                print("Json file modified")
        
        except Exception as e:
            print(e)

        finally:
            file.close()


    def create_inventory(self):
        '''
        Description:
            This method is used to create the inventory json file with the basic inputs.
        Parameter:
            This takes self as the parameter.
        Returns:
            This saves the inventory item detail in json file.
        '''
        inventory = {}
        try:
            name = input("Please enter the name of the item to be addded: ")
            inventory['name'] = name
            weight = input("Please enter the weight of the item in stock: ")
            inventory['weight'] = weight
            price = input("Please enter the price per kg of the item: ")
            inventory['price'] = price
            self.inventory_list.append(inventory)
            self.save()

        except ValueError:
            print("Invalid input")
        except Exception as e:
            print(e)


    def open(self):
        '''
        Description:
            This method just opens and loads the inventory list in our memory during runtime.
        Parameter:
            This takes self as the paramter.
        '''
        try:

            with open('C:/Users/subha/PythonBasics/OOPS/Inventory Management/Inventory.json', 'r') as file:
               self.inventory_list = json.load(file)
        
        except FileNotFoundError:
            print("File not found, please create it or check path!")

        except Exception as e:
            print(e)

    def edit_inventory(self):
        '''
        Description:
            This function is used to modify an already existing inventory.
        Parameter:
            It takes self as the parameter.
        '''
        try:
            self.open()
            if len(self.inventory_list) >= 1:
                name= input("Please enter the name of the item whoose values you want to change: ")
                for i in range(len(self.inventory_list)):
                    if self.inventory_list[i]['name'] == name:
                        num = int(input("Choose the part you want to edit: \n 1.Name  2.Weight  3.Price "))
                        if (num == 1):
                            new_name = input("Please enter the new name of the item: ")
                            self.inventory_list[i]['name'] = new_name
                            self.save()
                            break

                        elif (num == 2):
                            new_weight = input("Please enter the new available weight: ")
                            self.inventory_list[i]['weight'] = new_weight
                            self.save()
                            break
                        
                        elif (num == 3):
                            new_price = input("Please enter the new price per kg: ")
                            self.inventory_list[i]['price'] = new_price
                            self.save()
                            break
                        
                        else:
                            print("Invalid Selection.")

                    else:
                        print("No item with given name.")
            else:
                print("There are currently no entries")
        
        except ValueError:
            print("Invalid entry!")

        except Exception as e:
            print(e)


    def view(self):
        '''
        Description:
            This function is used to view all the inventory items.
        Parameter:
            This takes self as the parameter.
        '''
        self.open()
        try:
            if len(self.inventory_list) >= 1:
                 for i in range(len(self.inventory_list)):
                     print("Name of item-" ,self.inventory_list[i]['name'])
                     print("Available weight of item(kg)-" ,self.inventory_list[i]['weight'])
                     print("Price per kg of item-" ,self.inventory_list[i]['price'])
                     print("--------------------------------------------- \n")

            else:
                print("Currently empty inventory.")
        except Exception as e:
            print(e)

    
    def remove(self):
        '''
        Description:
            This method is used for deleting inventory details from the json file.
        Parameter:
            It takes self as a parameter to get inventory details stored inside list and
            delete the details and then save the json file.
        '''
        try:
            if len(self.inventory_list) >= 1:
                name = input("Enter the name of item you want to remove: ")
                for i in range(len(self.inventory_list)):
                    if ((self.inventory_list[i]['name']) == name): 
                        print(" Data Removed Successfully ")
                        del self.inventory_list[i]
                        self.save()
                        break
            else:
                print("There is nothing to delete")
                    
        except Exception as e:
            print(e)

                    



