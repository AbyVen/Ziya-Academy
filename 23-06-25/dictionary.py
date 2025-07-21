def main():
    contacts = {}

    while True:
        print("\nMenu:")
        print("1 - Add Contact")
        print("2 - View Contacts")
        print("3 - Update Contact")
        print("4 - Delete Contact")
        print("5 - Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter name: ")
            email = input("Enter email: ")
            phone = input("Enter phone number: ")
            contacts[name] = {'email': email, 'phone': phone}
            print(f"Contact for {name} added.")

        elif choice == '2':
            if not contacts:
                print("No contacts to display.")
            else:
                for name, info in contacts.items():
                    print(f"Name: {name}, Email: {info['email']}, Phone: {info['phone']}")

        elif choice == '3':
            name = input("Enter the name to update: ")
            if name in contacts:
                email = input("Enter new email: ")
                phone = input("Enter new phone number: ")
                contacts[name] = {'email': email, 'phone': phone}
                print(f"Contact for {name} updated.")
            else:
                print("Contact not found.")

        elif choice == '4':
            name = input("Enter the name to delete: ")
            if name in contacts:
                del contacts[name]
                print(f"Contact for {name} deleted.")
            else:
                print("Contact not found.")

        elif choice == '5':
            print("Exiting program.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()