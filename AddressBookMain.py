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

    
address_book = AddressBook()

contact1 = Contact("John", "Doe", "123 Elm St", "Springfield", "IL", "62701", "123-456-7890", "john.doe@example.com")
address_book.add_contact(contact1)
