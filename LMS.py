import datetime
import os
# os.getcsw()

class LMS:
    """This class is used to keep record of books library.
    It has total four modules: "Dispplay Books". "Return Books", "Add Books" """

    def __init__(self, list_of_books, library_name):
        self.list_of_books = list_of_books
        self.library_name = library_name
        self.book_dict = {}
        id = 101

        with open(self.list_of_books) as bk:
            content = bk.read()
        for line in content:
            self.book_dict.update({str(id) : {"book_title": line.replace("/n",""), "lender_name": "", "Issue_date": "", "status":"Available"}})

            id += 1
    def display_books(self):
        print("------------------------ List of Books ------------------------")
        print("Books ID", "\t", "Title")
        print("----------------------------------------------------------------")

        for key, value in self.book_dict.item():
            print(key, "\t\t", value.get("book_title"))