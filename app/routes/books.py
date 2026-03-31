from flask import Blueprint, jsonify, request
from app.schemas.book_schemas import BookCreate, BookUpdate, BookResponse
from app.services.library_service import LibraryService
from app.models.book import Book

books_bp = Blueprint('books', __name__)

@books_bp.route("/", methods=["GET"])
def get_books(service: LibraryService): # Injector сам підставить service
    books = service.list_books()
    return jsonify([BookResponse.model_validate(b).model_dump() for b in books])

@books_bp.route("/<int:book_id>", methods=["GET"])
def get_book(book_id: int, service: LibraryService):
    book = service.get_book(book_id)
    return jsonify(BookResponse.model_validate(book).model_dump())

@books_bp.route("/", methods=["POST"])
def create_book(service: LibraryService):
    data = BookCreate(**request.json)
    new_book = service.create_book(data)
    return jsonify(BookResponse.model_validate(new_book).model_dump()), 201

@books_bp.route("/<int:book_id>", methods=["PATCH"])
def update_book(book_id: int, service: LibraryService):
    data = BookUpdate(**request.json)
    updated = service.update_book(book_id, data)
    return jsonify(BookResponse.model_validate(updated).model_dump())

@books_bp.route("/<int:book_id>", methods=["DELETE"])
def delete_book(book_id: int, service: LibraryService):
    service.delete_book(book_id)
    return jsonify({"message": "Книгу успішно видалено"}), 200