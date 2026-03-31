# 📚 Library Management API (Backend)

## 🛠 Технологічний стек
* **Мова:** Python 3.11+
* **Менеджер пакетів:** `uv` (сучасна заміна pip/poetry)
* **Фреймворк:** Flask (з використанням Blueprints)
* **База даних:** PostgreSQL (запущена в Docker)
* **ORM:** SQLAlchemy 2.0 (сучасний декларативний стиль)
* **Міграції:** Alembic
* **DI (Dependency Injection):** Flask-Injector
* **Валідація та DTO:** Pydantic v2

## 🏗 Архітектура (Service-Repository Pattern)
Проект реалізовано за принципом розділення відповідальності:
1. **Routes (Контролери):** Тільки обробка HTTP запитів та виклик сервісів.
2. **Services (Бізнес-логіка):** Основні правила програми. Не залежать від HTTP або SQL деталей.
3. **Repositories (Доступ до даних):** Виконання SQL запитів через SQLAlchemy.
4. **Schemas (DTO):** Pydantic моделі для валідації вхідних даних та фільтрації вихідних.
5. **Models:** Опис таблиць бази даних.

## 🚀 Як запустити проект (Пам'ятка на завтра)

### 1. Підняти базу даних

Переконайся, що Docker запущений, і виконай:
```bash
docker-compose up -d
```

### 2. Встановити залежності
Використовуй uv для синхронізації віртуального оточення:

```bash
uv sync
```

### 3. Застосувати міграції
Онови структуру бази даних до останньої версії:

```bash
uv run alembic upgrade head
```
### 4. Запустити сервер

```bash
uv run python main.py
```
Додаток буде доступний за адресою: http://localhost:5000/api/books/

### 📝 Корисні команди Alembic
Створити нову міграцію:
- uv run alembic revision --autogenerate -m "Опис змін"

Застосувати міграцію:
- uv run alembic upgrade head

Відкотити останню міграцію:
- uv run alembic downgrade -1

✅ Поточний стан (Done)
- [x] Налаштовано Docker з PostgreSQL.

- [x] Реалізовано Dependency Injection (Flask-Injector).

- [x] Вирішено проблему циклічних імпортів (Book <-> Author).

- [x] Створено повний CRUD для Книг (Books).

- [x] Налаштовано глобальну обробку помилок (ValueError, ValidationError).

📅 План на наступну сесію
- Реалізувати аналогічний CRUD для Авторів (AuthorRepository, AuthorService).

- Налаштувати автоматичне завантаження імені автора при отриманні книги (Joined Load).

- Додати валідацію унікальності книг за назвою.

