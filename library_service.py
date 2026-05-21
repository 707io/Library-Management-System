from book import Book
from member import Member
from loan import Loan
from exceptions import (
    BookNotFoundError,
    MemberNotFoundError,
    BookNotAvailableError,
    BookAlreadyBorrowedError,
    InvalidOperationError
)


class LibraryService:
    def __init__(self):
        self.books = {}
        self.members = {}
        self.loans = []

    # BOOK OPERATIONS
    def add_book(self, book_id, title, author):
        if book_id in self.books:
            raise InvalidOperationError("Book already exists.")
        self.books[book_id] = Book(book_id, title, author)

    def get_book(self, book_id):
        if book_id not in self.books:
            raise BookNotFoundError("Book not found.")
        return self.books[book_id]

    # MEMBER OPERATIONS
    def add_member(self, member_id, name):
        if member_id in self.members:
            raise InvalidOperationError("Member already exists.")
        self.members[member_id] = Member(member_id, name)

    def get_member(self, member_id):
        if member_id not in self.members:
            raise MemberNotFoundError("Member not found.")
        return self.members[member_id]

    # LOAN OPERATIONS
    def borrow_book(self, member_id, book_id):
        book = self.get_book(book_id)
        member = self.get_member(member_id)

        if book.is_borrowed:
            raise BookAlreadyBorrowedError("Book is already borrowed.")

        book.is_borrowed = True
        member.borrowed_books.append(book)
        self.loans.append(Loan(book, member))

    def return_book(self, member_id, book_id):
        member = self.get_member(member_id)
        book = self.get_book(book_id)

        if book not in member.borrowed_books:
            raise BookNotAvailableError("This member did not borrow this book.")

        book.is_borrowed = False
        member.borrowed_books.remove(book)

        for loan in self.loans:
            if loan.book.book_id == book_id and loan.member.member_id == member_id and loan.return_date is None:
                loan.return_book()
                break

    def list_books(self):
        return [str(book) for book in self.books.values()]

    def list_members(self):
        return [str(member) for member in self.members.values()]

    def list_loans(self):
        return [str(loan) for loan in self.loans]