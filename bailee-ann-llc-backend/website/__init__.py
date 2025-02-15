from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase
from dotenv import load_dotenv
import os
from os import path



class Base(DeclarativeBase):
    pass
db = SQLAlchemy(model_class=Base)
DB_NAME = "/website/database.db"

def create_app():
    load_dotenv()
    app = Flask(__name__)

    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLALCHEMY_DATABASE_URI')
    db.init_app(app)
    #CORS(app)
    from .views import views
    from .auth import auth
    from website.api.routes import routes
    from website.api.auth_routes import auth_routes
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    app.register_blueprint(routes, url_prefix='/api')
    app.register_blueprint(auth_routes, url_prefix='/api')
    engine = create_engine(os.getenv('MYSQL_URI'), pool_pre_ping=True)
    from .models import User, Note
    with app.app_context():
        print("Attempting to create database...")
        
        db.create_all()
        print("databasd made")
    return app

    
