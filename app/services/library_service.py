from sqlalchemy import select

from app.models.book import Book
from app.repositories.book_repository import BookRepository
from app.schemas.book_schemas import BookCreate, BookUpdate


class LibraryService:
    def __init__(self, repository: BookRepository):
        self.repository = repository

    def list_books(self) -> list[Book]:
        print(f"DEBUG: self.repos is {self.repository}") # Додай це!
        return self.repository.get_all()

    def get_book(self, book_id: int) -> Book:
            book = self.repository.get_by_id(book_id)
            if not book:
                raise ValueError(f"Книгу з ID {book_id} не знайдено")
            return book
    
    def create_book(self, dto: BookCreate):
        return self.repository.create(**dto.model_dump())
    
    def update_book(self, book_id: int, dto: BookUpdate):
        data_to_update = dto.model_dump(exclude_unset=True)
        book = self.repository.update(book_id, **data_to_update)
        if not book:
            raise ValueError(f"Книгу з ID {book_id} не знайдено для оновлення")
        return self.repository.update(book_id, **data_to_update)
    
    def delete_book(self, book_id: int):
        success = self.repository.delete(book_id)
        if not success:
            raise ValueError(f"Неможливо видалити: книгу з ID {book_id} не знайдено")