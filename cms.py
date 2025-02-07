contactList = {}
def greeting():
    print("welcome to cms")
    print("please follow the instructions")
def file():
    with open("contact.txt", "w") as file:
        for key, value in contactList.items():
            file.write(f"{key}: {value}\n")

def seeFile():
    with open("contact.txt", "r") as file:
        content = file.read()
        print(content)
def loadFile():
    with open("contact.txt", "r") as file:
        content = file.read()
        # reading the lines
        lines = content.splitlines()
        for line in lines:
            if line.strip():
                try:
                    key,value = line.split(":",1)
                    contactList[key] = value
                except ValueError:
                    print(f"Line format error: {line}")
                    
                
            
              
            

    
def addName():
    print("add a new contact")
    while True:
        contactName =input("Enter the name of the contact or (enter * to go back to main menu): ")
        if contactName == "*":
            break
        contactName.upper()
        if contactName.isalpha():
            return addContact(contactName)
            
        else:
            print("Enter a valid input")
    
            
def addContact(name):
    while True:
        contactNumber = int(input(f"enter number of {name} or enter * to change the name: "))
        if contactNumber == "*":
            break
        
        return addingToDict(name,contactNumber)


        
    
def addingToDict(name, contact):
    print(f"name: {name}, contact: {contact}")
    contactList.update({name:contact})
    file()


def find():
    while True:
        name = input("Enter the name to find: ")
        if name.isalpha():
            if name in contactList:
                print(f"contact found: {name}: {contactList[name]}")
                break
            else:
                print(f"contact not found: {name}")
        else:
            print("Enter a valid input")

def change():
    while True:
        name = input("Enter the name to find or (enter * to back to main menu) : ")
        if name == "*":
            break
        if name.isalpha():
            if name in contactList:
                print(contactList[name])
                try:
                    #number = int(input("Enter the number to change"))
                    new_number = int(input("Enter the new number or (enter 0 to search name again): "))
                    if new_number == 0:
                        break
                    else:
                        contactList[name] = new_number  # Update the dictionary
                        contactList.update({name: new_number})  # Update the dictionary
                        print(contactList)
                        file()  # Save changes to the file
                        print(f"Updated {name}'s number to {new_number}")
                        break
                except ValueError:
                    print("Please enter a valid number")
            else:
                print(f"Contact {name} not found.")
                break
        else:
            print("Enter a valid name (letters only)")

                    
                
                
    
    
        
def addContactDetails():
    greeting()
    addName()

def userInput():
    while True:
        command = int(input("Enter 1 to add a new contact, 2 to to search between contact, 3 to make change, 4 for see all the contact lists and 0 to end: "))
        if command == 1:
            addContactDetails()
        elif command == 2:
            find()
        elif command ==3:
            change()
        elif command == 4:
            seeFile()
        elif command == 0:
            print("Thank you for using see you soon:")
            break
        else:
            print("Invalid command") 
        
       
            
            



            
    
loadFile()
userInput()


        




