from app import create_app
from dotenv import load_dotenv
import builtins
import sqlalchemy.orm
import os
import sys

builtins.Mapper = sqlalchemy.orm.Mapper

# 2. Реєструємо внутрішній тип _InfoType, який шукає Python 3.13
try:
    # Намагаємося дістати його з інтерфейсів SQLAlchemy
    from sqlalchemy.orm.interfaces import _InfoType
    builtins._InfoType = _InfoType
except ImportError:
    # Якщо не знайшли, просто кажемо Python, що це словник (чим він і є)
    builtins._InfoType = dict
print(f"--- ЗАПУЩЕНО НА ВЕРСІЇ: {sys.version} ---")
print(f"--- ШЛЯХ ДО PYTHON: {sys.executable} ---")
# Завантажуємо змінні з .env (DATABASE_URL тощо)
load_dotenv()

app = create_app()

if __name__ == "__main__":
    app.run(
        host="0.0.0.0", 
        port=int(os.getenv("PORT", 5000)), 
        debug=True
    )