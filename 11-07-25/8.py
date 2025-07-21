class Book:
    def __init__(self, title, copies):
        self.title = title
        self.copies = copies

    def borrow(self):
        if self.copies == 0:
            raise ValueError("No copies available to borrow.")
        self.copies -= 1
        print("Book borrowed.")

    def return_book(self):
        self.copies += 1
        print("Book returned.")

    def add_copies(self, n):
        self.copies += n
        print(n, "copies added.")

    def show(self):
        print(f"Available copies of '{self.title}': {self.copies}")


title = input("Enter book title: ")
copies = int(input("Enter number of copies: "))
book = Book(title, copies)

while True:
    print("\n1. Borrow Book\n2. Return Book\n3. Add Copies\n4. Show Copies\n5. Exit")
    choice = input("Choose an option: ")

    try:
        if choice == '1':
            book.borrow()
        elif choice == '2':
            book.return_book()
        elif choice == '3':
            count = int(input("How many copies to add? "))
            book.add_copies(count)
        elif choice == '4':
            book.show()
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")
    except ValueError as e:
        print("Error:", e)
