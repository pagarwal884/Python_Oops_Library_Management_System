import datetime

import os


class LMS:

    def __init__(self, list_of_books, library_name):
        self.list_of_books = list_of_books
        self.library_name = library_name
        self.book_dict = {}

        book_id = 101

        with open(self.list_of_books, "r") as bk:
            content = bk.readlines()

        for line in content:
            self.book_dict.update({
                str(book_id): {
                    "book_title": line.strip(),
                    "lender_name": "",
                    "issue_date": "",
                    "status": "Available"
                }
            })

            book_id += 1

    def display_books(self):
        print("\n------------------------ List of Books ------------------------")
        print("Book ID\t\tTitle\t\t\t\tStatus")
        print("---------------------------------------------------------------")

        for key, value in self.book_dict.items():
            print(
                key,
                "\t\t",
                value.get("book_title"),
                "\t\t",
                f"[{value.get('status')}]"
            )

    def issue_books(self):
        books_id = input("\nEnter book ID: ")

        if books_id in self.book_dict:

            if self.book_dict[books_id]["status"] != "Available":
                print(
                    f"\nThis book is already issued to "
                    f"{self.book_dict[books_id]['lender_name']} "
                    f"on {self.book_dict[books_id]['issue_date']}"
                )

                return self.issue_books()

            else:
                your_name = input("Enter your name: ")

                current_date = datetime.datetime.now().strftime(
                    "%d-%m-%Y %H:%M:%S"
                )

                self.book_dict[books_id]["lender_name"] = your_name
                self.book_dict[books_id]["issue_date"] = current_date
                self.book_dict[books_id]["status"] = "Already Issued"

                print(
                    f"\n{self.book_dict[books_id]['book_title']} "
                    f"Book Issued Successfully!"
                )

        else:
            print("\nBook not found!")

            return self.issue_books()

    def add_books(self):
        new_books = input("Enter the book title:")

        if new_books == "":
            return self.add_books()

        elif len(new_books) > 25:
            print(
                "Book title length is too long!! "
                "Title should be of 25 characters"
            )
            return self.add_books()

        else:
            with open(self.list_of_books, "a") as bk:
                bk.writelines(f"{new_books}\n")

                self.book_dict.update({
                    str(int(max(self.book_dict)) + 1): {
                        "book_title": new_books,
                        "lender_name": "",
                        "issue_date": "",
                        "status": "Available"
                    }
                })
                print(f"This book '{new_books}' has been added successfully!!!")
    def return_books(self):
        books_id = input("Enter your ID: ")

        if books_id in self.book_dict:
            if self.book_dict[books_id]["status"] == "Available":
                print(
                "This book is already available in library. "
                "Please check your book ID."
            )
                return self.return_books()
            elif not self.book_dict[books_id]["status"] == "Available":
                self.book_dict[books_id]["lender_name"] = ""
                self.book_dict[books_id]["issue_date"] = ""
                self.book_dict[books_id]["status"] = "Available"
                print("Successfully updated !!! \n")
            else:
                print("Book Id isn ot found")

try:
    myLMS = LMS("List_of_books.txt", "Python's Library")

    press_key_list = {
        "D": "Display Books",
        "I": "Issue Book",
        "A": "Add Book",
        "R": "Return Book",
        "Q": "Quit"
    }

    key_press = ""

    while key_press != "q":

        print(
            f"\n------------------------------------"
            f"Welcome to {myLMS.library_name} "
            f"Library Management System"
            f"------------------------------------\n"
        )

        for key, value in press_key_list.items():
            print("Press", key, "To", value)

        key_press = input("\nPress key: ").lower()

        if key_press == "i":
            print("\nCurrent Selection: Issue Book")
            myLMS.issue_books()

        elif key_press == "d":
            print("\nCurrent Selection: Display Books")
            myLMS.display_books()

        elif key_press == "a":
            print("\nCurrent Selection: Add Book")
            myLMS.add_books()

        elif key_press == "r":
            print("\nCurrent Selection: Return Book")
            myLMS.return_books()

        elif key_press == "q":
            print("\nThank you for using the Library Management System!")
            break

        else:
            print("\nInvalid selection! Please choose D, I, A, R, or Q.")

except FileNotFoundError:
    print("List_of_books.txt was not found.")

l = LMS("List_of_books.txt", "Python's Library")

l.display_books()