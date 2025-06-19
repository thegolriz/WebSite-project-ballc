from flask import Blueprint, jsonify
from website.models import User, Note
from website import db
from flask_jwt_extended import jwt_required, get_jwt_identity

routes = Blueprint('routes', __name__)

@routes.route('/hello', methods=['GET'])
def hello_world():
    return jsonify({"message": "Hello from the API"})
    
@routes.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()  
    users_list = [
        {"id": user.id, "email": user.email} for user in users
    ]
    return jsonify(users_list)

@routes.route('/notes', methods=['GET'])
def get_user_notes(user_id):
    notes = Note.query.filter_by(user_id=user_id).all()
    notes_list = [
        {"id": note.id, "data": note.data, "date": note.date.isoformat()}
        for note in notes
    ]
    return jsonify(notes_list)