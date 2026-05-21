class LibraryError(Exception):
    """Base class for library-related exceptions."""
    pass


class BookNotFoundError(LibraryError):
    pass


class MemberNotFoundError(LibraryError):
    pass


class BookNotAvailableError(LibraryError):
    pass


class BookAlreadyBorrowedError(LibraryError):
    pass


class InvalidOperationError(LibraryError):
    pass