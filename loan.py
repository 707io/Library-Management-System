from datetime import datetime

class Loan:
    def __init__(self, book, member):
        self.book = book
        self.member = member
        self.borrow_date = datetime.now()
        self.return_date = None

    def return_book(self):
        self.return_date = datetime.now()

    def __str__(self):
        status = "Returned" if self.return_date else "Active"
        return f"{self.book.title} -> {self.member.name} ({status})"