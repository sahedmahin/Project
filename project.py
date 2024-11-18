contacts = []

def display_contacts():
    if contacts:
        for index, contact in enumerate(contacts, start=1):
            print(f"{index}. Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")
    else:
        print("No contacts available.")

def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    contacts.append({'name': name, 'phone': phone, 'email': email})
    print(f"Contact {name} added successfully!")

def search_contact():
    name = input("Enter the name to search: ")
    found_contacts = [contact for contact in contacts if contact['name'].lower() == name.lower()]
    if found_contacts:
        for contact in found_contacts:
            print(f"Found - Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")
    else:
        print("No contact found with that name.")

def edit_contact():
    name = input("Enter the name of the contact to edit: ")
    for contact in contacts:
        if contact['name'].lower() == name.lower():
            print(f"Editing contact - Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")
            contact['name'] = input("Enter new name: ") or contact['name']
            contact['phone'] = input("Enter new phone number: ") or contact['phone']
            contact['email'] = input("Enter new email: ") or contact['email']
            print("Contact updated successfully!")
            return
    print("No contact found with that name.")

def delete_contact():
    name = input("Enter the name of the contact to delete: ")
    global contacts
    contacts = [contact for contact in contacts if contact['name'].lower() != name.lower()]
    print(f"Contact {name} deleted successfully!" if contacts else "No contact found to delete.")

def main_menu():
    while True:
        print("\nContact Management System")
        print("1. Display Contacts")
        print("2. Add Contact")
        print("3. Search Contact")
        print("4. Edit Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Choose an option (1-6): ")

        if choice == '1':
            display_contacts()
        elif choice == '2':
            add_contact()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            edit_contact()
        elif choice == '5':
            delete_contact()
        elif choice == '6':
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()
