# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a REST API for managing a small book catalog using FastAPI. Practice defining request models, handling HTTP methods, returning JSON, and reporting missing resources with appropriate status codes.

## 📝 Tasks

### 🛠️ Create Read Endpoints

#### Description
Use the provided `main.py` starter file to build endpoints that let clients list books and retrieve an individual book by its ID.

#### Requirements
Completed program should:

- Run locally with `uvicorn main:app --reload` and expose FastAPI's interactive documentation at `/docs`.
- Return the book catalog as JSON from `GET /books`.
- Return a matching book from `GET /books/{book_id}`.
- Return an HTTP 404 response when the requested book ID does not exist.

### 🛠️ Add Book Management Endpoints

#### Description
Extend the API so clients can add a book, update an existing book, and delete a book using the appropriate HTTP methods.

#### Requirements
Completed program should:

- Accept a book's title and author as a validated JSON request body using the provided `BookInput` model.
- Create a book with a unique ID using `POST /books` and return the created book with HTTP 201.
- Update the title and author of an existing book using `PUT /books/{book_id}` while keeping its ID unchanged.
- Return HTTP 404 when an update or delete request targets a book ID that does not exist.
- Delete a book using `DELETE /books/{book_id}` and return HTTP 204 on success.
