import os
import re
import json

contacts = {}

# User Interface (UI)
# Define the menu options
menu_options = {
    "1": "Add a new contact",
    "2": "Edit an existing contact",
    "3": "Delete a contact",
    "4": "Search for a contact",
    "5": "Display all contacts",
    "6": "Export contacts to a text file",
    "7": "Import contacts from a text file",
    "8": "Quit"
}

# Create a function to display the menu
def display_menu():
    print("Welcome to the Contact Management System!")
    for option, description in menu_options.items():
        print(f"{option}: {description}")

# Create a function to get user input
def get_user_input():
    while True:
        user_input = input("Enter your choice (1-8): ")
        if user_input.isdigit() and 1 <= int(user_input) <= 8:
            return int(user_input)
        else:
            print("Invalid input. Please try again.")

# Contact Data Storage
# Define a nested dictionary to store contact information
contact_data = {
    "name": "",
    "phone_number": "",
    "email": "",
    "additional_info": {}
}

# Define a function to add a new contact
def add_contact():
    contact_data["name"] = input("Enter name: ")
    contact_data["phone_number"] = input("Enter phone number: ")
    contact_data["email"] = input("Enter email address: ")
    contact_data["additional_info"] = {}
    # Add custom fields (optional)

# Define a function to edit an existing account
def edit_contact():
    contact_id = input("Enter the contact ID: ")
    if contact_id in contacts:
        # Update contact information
        pass
    else:
        print("Contact not found.")

# Define a function to delete a contact
def delete_contact():
    contact_id = input("Enter the contact ID: ")
    if contact_id in contacts:
        del contacts[contact_id]
        print("Contact deleted.")
    else:
        print("Contact not found.")

# Define a function to search for a contact
def search_contact():
    search_query = input("Enter search query: ")
    for contact_id, contact in contacts.items():
        if search_query in str(contact):
            print(f"Found contact {contact_id}: {contact}")
            break

# Define a function to display all contacts
def display_all_contacts():
    for contact_id, contact in contacts.items():
        print(f"Contact {contact_id}: {contact}")

# Define a function to export contacts to a text file
def export_contacts():
    with open("contacts.txt", "w") as f:
        for contact_id, contact in contacts.items():
            f.write(f"{contact_id}: {contact}\n")

# Define a function to import contacts from a text file
def import_contacts():
    with open("contacts.txt", "r") as f:
        for line in f.readlines():
            contact_id, contact_data = line.strip().split(":")
            contacts[contact_id] = json.loads(contact_data)

# Main Function
# Define the main function to run the application
def main():
    display_menu()
    while True:
        user_choice = get_user_input()
        if user_choice == 1:
            add_contact()
        elif user_choice == 2:
            edit_contact()
        elif user_choice == 3:
            delete_contact()
        elif user_choice == 4:
            search_contact()
        elif user_choice == 5:
            display_all_contacts()
        elif user_choice == 6:
            export_contacts()
        elif user_choice == 7:
            import_contacts()
        elif user_choice == 8:
            break

if __name__ == "__main__":
    main()