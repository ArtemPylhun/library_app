import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

# Завантажуємо змінні з .env
load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

# Виводимо в консоль при запуску
print("\n" + "="*30)
print(f"DEBUG: DATABASE_URL is: {DATABASE_URL}")
print("="*30 + "\n")

if not DATABASE_URL:
    print("❌ ПОМИЛКА: DATABASE_URL не знайдено в .env файлі!")

# 1. Engine — це "міст" до бази даних
engine = create_engine(DATABASE_URL)

# 2. SessionLocal — клас для створення сесій (конкретних підключень)
# autocommit=False: зміни не збережуться, поки ми не скажемо commit()
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# 3. Базовий клас для всіх моделей
class Base(DeclarativeBase):
    pass

# Функція-помічник для отримання сесії (зручно для Flask)
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()