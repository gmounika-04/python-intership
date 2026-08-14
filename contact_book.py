import json
import os

FILE_NAME = "contacts.json"


def load_contacts():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return {}


def save_contacts(contacts):
    with open(FILE_NAME, "w") as file:
        json.dump(contacts, file, indent=4)


def add_contact(contacts):
    name = input("Enter name: ").strip()
    phone = input("Enter phone number: ").strip()
    email = input("Enter email: ").strip()

    if not name or not phone:
        print("Name and phone number are required.")
        return

    contacts[name] = {
        "phone": phone,
        "email": email
    }

    save_contacts(contacts)
    print("Contact added successfully.")


def view_contacts(contacts):
    if not contacts:
        print("No contacts found.")
        return

    print("\n===== CONTACTS =====")

    for name, details in contacts.items():
        print(f"\nName  : {name}")
        print(f"Phone : {details['phone']}")
        print(f"Email : {details['email']}")


def search_contact(contacts):
    name = input("Enter name to search: ").strip()

    if name in contacts:
        details = contacts[name]

        print("\nContact found:")
        print(f"Name  : {name}")
        print(f"Phone : {details['phone']}")
        print(f"Email : {details['email']}")
    else:
        print("Contact not found.")


def update_contact(contacts):
    name = input("Enter name to update: ").strip()

    if name not in contacts:
        print("Contact not found.")
        return

    phone = input("Enter new phone number: ").strip()
    email = input("Enter new email: ").strip()

    if phone:
        contacts[name]["phone"] = phone

    if email:
        contacts[name]["email"] = email

    save_contacts(contacts)
    print("Contact updated successfully.")


def delete_contact(contacts):
    name = input("Enter name to delete: ").strip()

    if name in contacts:
        del contacts[name]
        save_contacts(contacts)
        print("Contact deleted successfully.")
    else:
        print("Contact not found.")


def main():
    contacts = load_contacts()

    while True:
        print("\n===== CONTACT BOOK =====")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_contact(contacts)

        elif choice == "2":
            view_contacts(contacts)

        elif choice == "3":
            search_contact(contacts)

        elif choice == "4":
            update_contact(contacts)

        elif choice == "5":
            delete_contact(contacts)

        elif choice == "6":
            print("Thank you for using Contact Book!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()