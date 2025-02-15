#This file holds the api's for the website
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .routes import routes
from .auth_routes import auth_routes

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'thisissecure'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////Users/anisgolriz/Desktop/bailee_ann_site/bailee-ann-llc-backend/website/database.db'

    db.init_app(app)

    
    app.register_blueprint(routes, url_prefix='/api')  # Add URL prefix

    return app



