from library_service import LibraryService
from exceptions import LibraryError


def menu():
    print("\n===Library Management System===")
    print("1. Add Book")
    print("2. Register Member")
    print("3. Borrow Book")
    print("4. Return Book")
    print("5. View Books")
    print("6. View Members")
    print("7. View Loans")
    print("8. Exit")


def main():
    library = LibraryService()

    while True:
        menu()
        choice = input("Choose an option: ")

        try:
            if choice == "1":
                book_id = input("Book ID: ")
                title = input("Title: ")
                author = input("Author: ")
                library.add_book(book_id, title, author)
                print("Book added successfully.")

            elif choice == "2":
                member_id = input("Member ID: ")
                name = input("Name: ")
                library.add_member(member_id, name)
                print("Member registered successfully.")

            elif choice == "3":
                member_id = input("Member ID: ")
                book_id = input("Book ID: ")
                library.borrow_book(member_id, book_id)
                print("Book borrowed successfully.")

            elif choice == "4":
                member_id = input("Member ID: ")
                book_id = input("Book ID: ")
                library.return_book(member_id, book_id)
                print("Book returned successfully.")

            elif choice == "5":
                print("\nBooks:")
                for b in library.list_books():
                    print(b)

            elif choice == "6":
                print("\nMembers:")
                for m in library.list_members():
                    print(m)

            elif choice == "7":
                print("\nLoans:")
                for l in library.list_loans():
                    print(l)

            elif choice == "8":
                print("Exiting system...")
                break

            else:
                print("Invalid option. Try again.")

        except LibraryError as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    main()