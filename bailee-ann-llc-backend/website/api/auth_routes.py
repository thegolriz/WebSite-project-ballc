from flask import Blueprint, request, jsonify
from werkzeug.security import check_password_hash
from website.models import User
from website import db

auth_routes = Blueprint('auth_routes', __name__)

@auth_routes.route('/login', methods=['GET', 'POST'])
def login_api():
    if request.method == 'POST':
        data = request.get_json()
        email = data.get('email')
        password = data.get('password')

        user = User.query.filter_by(email=email).first()

        if user and check_password_hash(user.password, password):
            return jsonify({"message": "Login successful"}), 200
        else:
            return jsonify({"error": "Invalid email or password"}), 401

    return jsonify({"message": "Login endpoint"}), 200

@auth_routes.route('/logout', methods=['GET','POST'])
def logout_api():
    return jsonify({"message": "Logout endpoint"}), 200
@auth_routes.route('/signup', methods =['GET','POST'])
def signup_api():
    if request.method == 'POST':
        data= request.get_json()
        email= data.get('email')
        firstName = data.get('firstName')
        password = data.get('password')
        existing = User.query.filter_by(email=email).first()
        if existing:
            return jsonify({"error":"email in use"}),401
        else:
            return jsonify({"message":"account created"}),200
        
    return jsonify({"message":"Signup endpoint"}),200