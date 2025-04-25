class contact:
    def __init__(self, phone_number, name, email ):
        self.phone_number = phone_number
        self.name = name
        self.email = email
        
    def __str__(self):
        return f"Name: {self.name}    number: {self.phone_number}    email: {self.email}"


Vincent = contact("123-456-7899", "Vincent", "Vincent@gmail.com")
print(Vincent)
John = contact("987-654-3211", "John", "John@gmail.com")
print(John)


class delete_contact:
    def __init__(self, remove_contact):
        

        self.remove_contact = remove_contact
    def __str__(self):
        return f"You have succesfully removed: {self.remove_contact},  from your contacts list."

John = delete_contact ("John")
print(John)
print(Vincent)

class add_contact:
    def __init__(self, add_contact):
        self.add_contact = add_contact
    def __str__(self):
        return f"You have succesfully added: {self.add_contact}, to your contacts list."
John = add_contact ("John")
print(John)
print(Vincent)

#ContactBook class
#Create a class called 'ContactBook' to represent a group of contacts. It should have the following features.

#properties
#contacts - a list containing all available contacts
#methods
#add_contact - adds a new contact
#delete_contact - deletes the contact
#search_contact(name): bool - returns true if there is a contact with the input name.
#display_contacts - prints out all of the contacts in your Contact list.


#creat the class



    
