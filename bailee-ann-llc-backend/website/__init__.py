from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from dotenv import load_dotenv
from flask_jwt_extended import JWTManager, create_access_token, create_refresh_token, jwt_required, get_jwt_identity
import os
from os import path
from flask_migrate import Migrate




class Base(DeclarativeBase):
    pass
db = SQLAlchemy(model_class=Base)
migrate = Migrate()


def create_app():
    load_dotenv()
    app = Flask(__name__)
    #app configs here
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLALCHEMY_DATABASE_URI')
    #jwt configs bewloer
    app.config["JWT_SECRET_KEY"] = os.getenv('JWT_SECRET_KEY')
    app.config["JWT_ACCESS_TOKEN_EXPIRES"] = 3600
    app.config["JWT_REFRESH_TOKEN_EXPIRES"] = 86400
    db.init_app(app)
    jwt = JWTManager(app)
    #done
   
    
    from website.api.routes import routes
    from website.api.auth_routes import auth_routes
    app.register_blueprint(routes, url_prefix='/api')
    app.register_blueprint(auth_routes, url_prefix='/api')
    from .models import User, Note
    return app
    


    
