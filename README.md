# Library Management System

## Overview

The **Library Management System** is a simple Python-based console application designed to manage books, members, and borrowing transactions in a library. The system demonstrates the use of **Object-Oriented Programming (OOP)** concepts such as classes, objects, encapsulation, and exception handling.

This project allows users to:

* Add and manage books
* Register library members
* Borrow and return books
* View books, members, and loan records
* Handle errors using custom exceptions

---

# Features

## Book Management

* Add new books to the library
* Store book details such as:

  * Book ID
  * Title
  * Author
* Track whether a book is available or borrowed

## Member Management

* Register new members
* Store member information:

  * Member ID
  * Name
* Track borrowed books per member

## Loan Management

* Borrow books
* Return books
* Record active and returned loans

## Exception Handling

The system includes custom exceptions for handling errors such as:

* Book not found
* Member not found
* Book already borrowed
* Invalid operations

---

# Project Structure

```bash
Library-Management-System/
│
├── main.py                 # Main program and menu interface
├── library_service.py      # Core system operations
├── book.py                 # Book class
├── member.py               # Member class
├── loan.py                 # Loan class
├── exceptions.py           # Custom exception classes
└── README.md               # Documentation
```

---

# Requirements

* Python 3.x

No external libraries are required.

---

# How to Run

1. Download or clone the project.

2. Open a terminal in the project folder.

3. Run the program:

```bash
python main.py
```

---

# Menu Options

When the program starts, the following menu will appear:

```text
=== Library Management System ===
1. Add Book
2. Register Member
3. Borrow Book
4. Return Book
5. View Books
6. View Members
7. View Loans
8. Exit
```

---

# Sample Usage

## Add a Book

```text
Book ID: B001
Title: Python Basics
Author: John Doe
Book added successfully.
```

## Register a Member

```text
Member ID: M001
Name: Austine
Member registered successfully.
```

## Borrow a Book

```text
Member ID: M001
Book ID: B001
Book borrowed successfully.
```

## Return a Book

```text
Member ID: M001
Book ID: B001
Book returned successfully.
```

---

# Classes Used

## Book

Represents a book in the library.

### Attributes

* `book_id`
* `title`
* `author`
* `is_borrowed`

---

## Member

Represents a library member.

### Attributes

* `member_id`
* `name`
* `borrowed_books`

---

## Loan

Represents a borrowing transaction.

### Attributes

* `book`
* `member`
* `borrow_date`
* `return_date`

---

## LibraryService

Handles all library operations including:

* Adding books
* Registering members
* Borrowing books
* Returning books
* Listing records

---

# OOP Concepts Applied

* **Encapsulation** – Data and methods are grouped into classes.
* **Abstraction** – Library operations are managed through the `LibraryService` class.
* **Object Composition** – Loans connect books and members.
* **Exception Handling** – Custom exceptions improve reliability and error management.

---

# License

This project is for educational purposes only.
