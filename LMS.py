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


l = LMS("List_of_books.txt", "Python's Library")

l.display_books()