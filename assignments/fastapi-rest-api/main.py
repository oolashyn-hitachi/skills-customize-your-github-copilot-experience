from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel

app = FastAPI(title="Book Catalog API")


class BookInput(BaseModel):
    title: str
    author: str


books = [
    {"id": 1, "title": "The Hobbit", "author": "J.R.R. Tolkien"},
    {"id": 2, "title": "A Wrinkle in Time", "author": "Madeleine L'Engle"},
]


@app.get("/books")
def list_books():
    return books


@app.get("/books/{book_id}")
def get_book(book_id: int):
    # TODO: Find the book by ID or raise an HTTP 404 error.
    raise NotImplementedError


@app.post("/books", status_code=status.HTTP_201_CREATED)
def create_book(book: BookInput):
    # TODO: Assign a unique ID, save the book, and return it.
    raise NotImplementedError


@app.put("/books/{book_id}")
def update_book(book_id: int, book: BookInput):
    # TODO: Update the matching book or raise an HTTP 404 error.
    raise NotImplementedError


@app.delete("/books/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_book(book_id: int):
    # TODO: Delete the matching book or raise an HTTP 404 error.
    raise NotImplementedError
