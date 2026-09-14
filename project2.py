#LIBRARY MANAGEMENT SYSTEM

print("\n******** Welcome to Library Management System ********")

# Library books
library = ["Book A", "Book B", "Book C", "Book D"]

# Issued books
issued_books = {}

# Members
members = {}


def view_library():
    """Display available books."""
    print("\n******** Available Books ********")

    if not library:
        print("No books are currently available.")
    else:
        for i, book in enumerate(library, start=1):
            print(f"{i}. {book}")


def add_book():
    """Add a new book to the library."""
    book = input("Enter book name: ").strip().title()

    if not book:
        print("Book name cannot be empty.")
    elif book in library:
        print(f"'{book}' is already in the library.")
    else:
        library.append(book)
        print(f"'{book}' added successfully.")


def remove_book():
    """Remove a book from the library."""
    book = input("Enter book name: ").strip().title()

    if book in library:
        library.remove(book)
        print(f"'{book}' removed successfully.")
    else:
        print(f"'{book}' does not exist in the library.")


def replace_book():
    """Replace an existing book with a new book."""
    old_book = input("Enter old book name: ").strip().title()

    if old_book not in library:
        print(f"'{old_book}' does not exist in the library.")
        return

    new_book = input("Enter new book name: ").strip().title()

    if not new_book:
        print("New book name cannot be empty.")
        return

    if new_book in library:
        print(f"'{new_book}' already exists in the library.")
        return

    index = library.index(old_book)
    library[index] = new_book

    print(f"'{old_book}' has been replaced with '{new_book}'.")


def book_management():
    """Book management menu."""
    while True:
        print("\n******** Book Management ********")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. Replace Book")
        print("4. Back to Main Menu")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            add_book()
        elif choice == "2":
            remove_book()
        elif choice == "3":
            replace_book()
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please enter 1-4.")


def membership():
    """Add and display member information."""
    print("\n******** Membership ********")

    member = input("Are you a member? (yes/no): ").strip().lower()

    if member == "yes":
        print("Please enter your member details.")

    elif member == "no":
        print("\nFor membership, enter your details below.")
    else:
        print("Please enter only yes or no.")
        return

    name = input("Enter your name: ").strip()
    age = input("Enter your age: ").strip()
    member_id = input("Enter your ID: ").strip()
    contact = input("Enter your contact: ").strip()
    address = input("Enter your address: ").strip()
    valid_till = input("Enter membership validity date: ").strip()

    members[member_id] = {
        "name": name,
        "age": age,
        "contact": contact,
        "address": address,
        "valid_till": valid_till
    }

    print("\nMember added successfully.")
    print("\n------ Library Card Details ------")
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"ID: {member_id}")
    print(f"Contact: {contact}")
    print(f"Address: {address}")
    print(f"Valid Till: {valid_till}")


def issue_book():
    """Issue a book to a member."""
    book = input("Enter book name: ").strip().title()

    if book not in library:
        print(f"'{book}' is not available in the library.")
        return

    member_id = input("Enter member ID: ").strip()

    if member_id not in members:
        print("Member not found. Please register first.")
        return

    due_date = input("Enter due date (DD-MM-YYYY): ").strip()

    library.remove(book)

    issued_books[book] = {
        "member_id": member_id,
        "due_date": due_date
    }

    print(f"\n'{book}' issued successfully.")
    print(f"Due date: {due_date}")


def return_book():
    """Return an issued book."""
    book = input("Enter book name: ").strip().title()

    if book not in issued_books:
        print(f"'{book}' is not currently issued.")
        return

    return_date = input("Enter return date (DD-MM-YYYY): ").strip()
    due_date = issued_books[book]["due_date"]

    library.append(book)
    del issued_books[book]

    print(f"\n'{book}' returned successfully.")
    print(f"Due date: {due_date}")
    print(f"Return date: {return_date}")

    print("\nNote: Enter dates in DD-MM-YYYY format.")
    print("For this beginner version, fine calculation is not automatic.")


def issue_return_menu():
    """Issue or return book menu."""
    while True:
        print("\n******** Issue / Return Book ********")
        print("1. Issue Book")
        print("2. Return Book")
        print("3. Back to Main Menu")

        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            issue_book()
        elif choice == "2":
            return_book()
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please enter 1-3.")


def fine_management():
    """Manage fines for late returns."""
    print("\n******** Fine Management ********")

    book = input("Enter book name: ").strip().title()

    if book not in issued_books:
        print(f"'{book}' is not currently issued.")
        return

    due_date = issued_books[book]["due_date"]
    return_date = input("Enter return date: ").strip()

    print(f"\nDue date: {due_date}")
    print(f"Return date: {return_date}")

    print("\nFor this version, fine amount is entered manually.")
    fine = input("Enter fine amount (Rs): ").strip()

    if fine.isdigit():
        fine = int(fine)

        if fine > 0:
            print(f"Fine for '{book}': Rs/{fine}")

            paid = input("Has the fine been paid? (yes/no): ").strip().lower()

            if paid == "yes":
                print("Fine paid successfully.")
            else:
                print("Fine is still pending.")
        else:
            print("No fine required.")
    else:
        print("Please enter a valid numeric fine amount.")


def main():
    """Main program."""
    while True:
        print("\n======================================")
        print("       LIBRARY MANAGEMENT SYSTEM")
        print("======================================")
        print("1. View Library")
        print("2. Book Management")
        print("3. Membership")
        print("4. Issue / Return Book")
        print("5. Fine Management")
        print("6. Exit")

        choice = input("\nEnter your choice (1-6): ").strip()

        if choice == "1":
            view_library()

        elif choice == "2":
            book_management()

        elif choice == "3":
            membership()

        elif choice == "4":
            issue_return_menu()

        elif choice == "5":
            fine_management()

        elif choice == "6":
            print("\nThank you for using Library Management System.")
            print("Come again!")
            break

        else:
            print("Invalid choice. Please enter a number from 1-6.")


# Start the program
if __name__ == "__main__":
    main()
