from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    # Configuração do banco de dados com SQLAlchemy
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv(
        'DATABASE_URL', 'postgresql://eduflix_user:eduflix_pass@db:5432/eduflix_db'
    )
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Inicializar o SQLAlchemy
    db.init_app(app)

    @app.route("/")
    def home():
        return "Bem-vindo ao Eduflix!"

    return app
