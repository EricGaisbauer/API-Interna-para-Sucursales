from flask import Flask
from flask_cors import CORS
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
ma = Marshmallow()
def create_app():
    app = Flask(__name__, static_folder='my-vite-app/public')
    
    # Configuración de la base de datos
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root@localhost/ferreteria'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    db.init_app(app)
    ma.init_app(app)
    CORS(app)
    
    with app.app_context():
        from . import routes, models,schemas
        db.create_all()

    return app