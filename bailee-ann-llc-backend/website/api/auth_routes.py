from flask import Blueprint, request, jsonify
from werkzeug.security import check_password_hash
from flask_jwt_extended import create_access_token, create_refresh_token,jwt_required, get_jwt_identity
from website.models import User
from website import db


auth_routes = Blueprint('auth_routes', __name__)
#the login api is down below
@auth_routes.route('/login', methods=['POST'])
def login_api():
    
    data = request.get_json()
    if not data or 'email' not in data or 'password' not in data:
        return jsonify({"error": "Missing email and/or password"}), 400
    email = data['email']
    password = data['password']

    user = User.query.filter_by(email=email).first()

    if user and check_password_hash(user.password, password):
        access_token = create_access_token(identity = str(user.id))
        refresh_token = create_refresh_token(identity = str(user.id))
        return jsonify({"access_token":access_token, 
                       "refresh_token":refresh_token,
                       "expires in": 3600}), 200
    else:
        return jsonify({"error": "Invalid email or password"}), 401
     
#the protected login using jwt is below
@auth_routes.route('/protected', methods=['GET'])
@jwt_required()
def protected():
    print("Received Headers:")
    auth_header = request.headers.get("Authorization")
    print(f"Received Authorization Header: {auth_header}") 
    user_id = get_jwt_identity()
    print(f"Extracted user ID from JWT: {user_id}") 
    user = User.query.get(user_id)
   
    if not user:
        return jsonify({"error": "user not found"}),401
    return jsonify({"message": f"Hello user {user.email}!"}), 200


#token refresh is below
@auth_routes.route('/refresh', methods=["POST"])
@jwt_required(refresh=True)#requries existing token
def refresh():
    user_id = get_jwt_identity()
    new_token = create_access_token(identity=user_id)
    return jsonify(access_token= new_token),200

#logout is below
@auth_routes.route('/logout', methods=['GET','POST'])
def logout_api():
    return jsonify({"message": "Logout endpoint"}), 200

#signup is below
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