'''
    @Author: Sudhanshu Kumar
    @Date: 07-11-2024
    @Last Modified by: Sudhanshu Kumar
    @Last Modified time: 07-11-2024
    @Title : Address Book 

'''

import logger

log = logger.logger_init('AddressBook')

class Contact:
    def __init__(self, first_name, last_name, address, city, state, zip_code, phone, email):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.phone = phone
        self.email = email

    def __str__(self):
        return (f"{self.first_name} {self.last_name}, {self.address}, {self.city}, {self.state}, {self.zip_code}, {self.phone}, {self.email}")

class AddressBook:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, contact):
        key = f"{contact.first_name} {contact.last_name}"
        if key not in self.contacts:
            self.contacts[key] = contact
            log.info(self.contacts.items())
            log.info(f"Contact {key} added successfully.")
        else:
            log.info(f"Contact {key} already exists in the address book.")

    def display_contacts(self):
        if self.contacts:
            for contact in self.contacts.values():
                log.info(contact)
        else:
            log.info("No contacts in the address book.")

    
class AddressBookMain:
    def __init__(self):
        self.address_book = AddressBook()

    def add_contact_from_console(self):
        print("Enter the following contact details:")

        first_name = input("First Name: ")
        last_name = input("Last Name: ")
        address = input("Address: ")
        city = input("City: ")
        state = input("State: ")
        zip_code = input("Zip Code: ")
        phone = input("Phone Number: ")
        email = input("Email: ")

        contact = Contact(first_name, last_name, address, city, state, zip_code, phone, email)
        self.address_book.add_contact(contact)

    def run(self):
        while True:
            print("\n--- Address Book ---")
            print("1. Add New Contact")
            print("6. Display Contact")
            print("7.Exit")
    
            choice = input("Enter your choice: ")

            if choice == "1":
                self.add_contact_from_console()
            elif choice == "6":
                self.address_book.display_contacts()
                break
            elif choice =="7":
                break
            else:
                print("Invalid choice. Please try again.")


if __name__=="__main__":
    address_main = AddressBookMain()
    address_main.run()
