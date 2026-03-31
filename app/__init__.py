from flask import Flask, jsonify
from flask_injector import FlaskInjector
from pydantic import ValidationError
from app.di import AppModule
from app.routes.books import books_bp

def create_app():
    app = Flask(__name__)

    # Реєстрація маршрутів (Blueprint)
    app.register_blueprint(books_bp, url_prefix="/api/books")

    @app.errorhandler(ValueError)
    def handle_business_errors(e):
        """Ловить помилки з сервісів (наприклад, 'Книгу не знайдено')"""
        return jsonify({"error": str(e)}), 400
    
    @app.errorhandler(ValidationError)
    def handle_pydantic_errors(e):
        """Ловить помилки валідації Pydantic (невірний тип даних)"""
        return jsonify({"validation_error": e.errors()}), 422

    FlaskInjector(app=app, modules=[AppModule()])
    return app