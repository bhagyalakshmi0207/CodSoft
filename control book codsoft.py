contacts = []  
def add_contact():
    name= input("Enter a contact name:")
    phone_number = input("Enter phone number:")
    email = input("Enter email:")
    address = input("Enter address:")
    contact = {"name": name, "phone_number": phone_number, "email": email, "address": address}
    contacts.append(contact)
    print("Contact added successfully!")

def view_contacts():
    if not contacts:
        print("There are no contacts saved yet.")
        return

    print("Contacts:")
    for i, contact in enumerate(contacts):
        name = contact["name"]
        phone_number = contact.get("phone_number")  
        print(f"{i+1}. {name} - {phone_number}")

def search_contact():
    search_term = input("Enter search term: ")
    found_contacts = []
    for contact in contacts:
        if search_term in contact.get("phone_number", ""):
            found_contacts.append(contact)

    if found_contacts:
        print("Search results:")
        for i, contact in(found_contacts):
            name = contact["name"]
            phone_number = contact.get("phone_number")
            email = contact.get("email")
            address = contact.get("address")
            print(f"{i+1}. {name},{phone_number}\n  Email: {email}\n  Address: {address}")
    else:
        print("No contacts found for", search_term)
def update_contact():
     name = input("Enter the name of the contact to update:")
     for contact in contacts:
        if contact["name"] == name:
            print("Enter new details:")
            new_name = input(f"Name ({contact['name']}): ")
            new_phone = input(f"Phone ({contact['phone']}): ")
            new_email = input(f"Email ({contact['email']}): ")
            new_address = input(f"Address ({contact['address']}): ")

            if new_name:
                contact["name"] = new_name
            if new_phone:
                contact["phone"] = new_phone
            if new_email:
                contact["email"] = new_email
            if new_address:
                contact["address"] = new_address

            print("Contact updated successfully!")
            return
        print("Contact not found.")

def delete_contact():
    name = input("Enter the name of the contact to delete: ")
    for i,contact in enumerate(contacts):
        if contact["name"] == name:
            del contacts[i]
            print("Contact deleted successfully!")
            return
    print("Contact not found.")

def menu():
    print("Contact Book")
    print("Press 1 to Add Contact:")
    print("Press 2 to View Contact:")
    print("Press 3 to Search Contact:")
    print("Press 4 to Update Contact:")
    print("Press 5 to Delete Contact:")
    print("Press 6 to Exit:")

def main():
    while True:
        menu()
        choice = input("Enter choice (1/2/3/4/5/6): ")
        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            update_contact()
        elif choice == '5':
            delete_contact()
        elif choice == '6':
            print("Exit:")
            break
        else:
            print("Invalid")

if __name__ == "__main__":
    main()

