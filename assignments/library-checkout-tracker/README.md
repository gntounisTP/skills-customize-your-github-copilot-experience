# 📘 Assignment: Library Checkout Tracker

## 🎯 Objective

Build a FastAPI application that stores library books and checkout records in SQLite. You will practice persistent data storage, CRUD operations, request validation, and API design.

## 📝 Tasks

### 🛠️ Set Up the Database and Read Endpoints

#### Description
Create a FastAPI app for a small library system. Set up a SQLite database, create a `books` table, and add endpoints to view all books or a single book by ID.

#### Requirements
Completed program should:

- Create a FastAPI app instance
- Create or connect to a SQLite database file
- Create a `books` table with fields such as `id`, `title`, `author`, and `checked_out`
- Add a `GET /books` endpoint that returns all books from the database
- Add a `GET /books/{book_id}` endpoint that returns one book or a clear error if it does not exist


### 🛠️ Add Checkout, Update, and Delete Operations

#### Description
Extend the API so users can add books, update book details, check books in or out, and remove books from the system.

#### Requirements
Completed program should:

- Define a Pydantic model for incoming book data
- Add a `POST /books` endpoint to create a new book record
- Add a `PUT /books/{book_id}` endpoint to update an existing book
- Add a `PATCH /books/{book_id}/checkout` endpoint to change checkout status
- Add a `DELETE /books/{book_id}` endpoint to remove a book and return appropriate success or error responses