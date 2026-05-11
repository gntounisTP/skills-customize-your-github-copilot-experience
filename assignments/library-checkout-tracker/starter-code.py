import sqlite3

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel


app = FastAPI(title="Library Checkout Tracker")
DATABASE_NAME = "library.db"


class Book(BaseModel):
    title: str
    author: str
    checked_out: bool = False


def get_connection():
    return sqlite3.connect(DATABASE_NAME)


def initialize_database():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            author TEXT NOT NULL,
            checked_out INTEGER NOT NULL DEFAULT 0
        )
        """
    )

    connection.commit()
    connection.close()


@app.on_event("startup")
def startup():
    initialize_database()


@app.get("/")
def read_root():
    return {"message": "Welcome to the Library Checkout Tracker API"}


@app.get("/books")
def get_books():
    # TODO: Query the database and return all books.
    return {"message": "Implement listing all books"}


@app.get("/books/{book_id}")
def get_book(book_id: int):
    # TODO: Return one book by id or raise HTTPException(status_code=404).
    raise HTTPException(status_code=404, detail="Book not found")


@app.post("/books")
def create_book(book: Book):
    # TODO: Insert the new book into the database and return the created record.
    return {"message": "Implement book creation", "book": book.model_dump()}


@app.put("/books/{book_id}")
def update_book(book_id: int, book: Book):
    # TODO: Update the matching book or raise HTTPException(status_code=404).
    return {
        "message": "Implement book update",
        "book_id": book_id,
        "book": book.model_dump(),
    }


@app.patch("/books/{book_id}/checkout")
def toggle_checkout(book_id: int):
    # TODO: Toggle the checked_out value for the selected book.
    return {"message": f"Implement checkout toggle for book {book_id}"}


@app.delete("/books/{book_id}")
def delete_book(book_id: int):
    # TODO: Delete the matching book or raise HTTPException(status_code=404).
    return {"message": f"Implement deletion for book {book_id}"}


# Run locally with:
# uvicorn starter-code:app --reload