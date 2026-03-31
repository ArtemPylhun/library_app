from sqlalchemy import select
from sqlalchemy.orm import Session
from app.models.book import Book
from sqlalchemy.orm import Mapper


class BookRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_all(self) -> list[Book]:
        stmt = select(Book).order_by(Book.id)
        return list(self.db.scalars(stmt).all())

    def get_by_id(self, book_id: int) -> Book:
        return self.db.get(Book, book_id)
    
    def update(self, book_id: int, **update_data) -> Book | None:
        book = self.get_by_id(book_id)
        if not book:
            return None
        
        for key, value in update_data.items():
            if hasattr(book, key):
                setattr(book, key, value)
                
        self.db.commit()
        self.db.refresh(book)
        return book
    
    def create(self, title: str, author_id: int) -> Book:
        book = Book(title=title, author_id=author_id)
        self.db.add(book)
        self.db.commit()
        self.db.refresh(book)
        return book
    
    def delete(self, book_id: int) -> bool:
        book = self.get_by_id(book_id)
        if book:
            self.db.delete(book)
            self.db.commit()
            return True
        return False