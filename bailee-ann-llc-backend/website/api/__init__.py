#This file holds the api's for the website
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os
from .routes import routes
from .auth_routes import auth_routes

db = SQLAlchemy()

def create_app():
    load_dotenv()
    app = Flask(__name__)
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLALCHEMY_DATABASE_URI')
    db.init_app(app)

    app.register_blueprint(routes, url_prefix='/api')  # Add URL prefix
    app.register_blueprint(auth_routes, url_prefix='/api') 

    return app



