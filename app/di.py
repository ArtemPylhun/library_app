from typing import Generator
from injector import Module, provider, singleton
from sqlalchemy.orm import Session
from app.database import SessionLocal, engine
from app.repositories.book_repository import BookRepository
from app.services.library_service import LibraryService


class AppModule(Module):
    @provider
    def provide_db_session(self) -> Generator[Session, None, None]:
        db = SessionLocal(bind=engine) 
        try:
            yield db
        finally:
            db.close()

    @provider
    def provide_book_repo(self, db: Session) -> BookRepository:
        return BookRepository(db=db)
    
    @provider
    @singleton
    def provide_library_service(self, repo: BookRepository) -> LibraryService:
        return LibraryService(repository=repo)