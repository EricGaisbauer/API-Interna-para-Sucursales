from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from .config import Config  # Importación relativa

db = SQLAlchemy()
ma = Marshmallow()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    ma.init_app(app)

    from .routes import init_routes  # Importación relativa
    init_routes(app)

    with app.app_context():
        db.create_all()
    return app
