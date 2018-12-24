from flask import request, jsonify, current_app
from itsdangerous import (TimedJSONWebSignatureSerializer as Serializer, BadSignature, SignatureExpired)
from werkzeug.security import generate_password_hash, check_password_hash
from resources.models.user import User

class Auth:

    @staticmethod
    def _generate_token(payload):
        serializer = Serializer(current_app.config['SECRET_KEY'], expires_in=3600)
        return serializer.dumps(payload).decode(encoding='ascii')


    @staticmethod
    def _verify_token(token):
        serializer = Serializer(current_app.config['SECRET_KEY'])
        try:
            data = serializer.loads(token)
        except BadSignature or SignatureExpired:
            return None


    @staticmethod
    def _verify_password(password, user):
        return check_password_hash(user.password_hash, password)


    @classmethod
    def register(cls):
        params = request.json
        if params['password'] != params['verify_password']:
            raise ValueError('Password and Verify Password are not the same')

        user = User.post(params)
        if user:
            token = Auth._generate_token({"username": user.username, "id": user.get_id})

        return jsonify({
            "status": True,
            "username": user.username,
            "token": token
        })


    @classmethod
    def login(cls):
        username, password = request.json['username'], request.json['password']
        user = User.find_by_username(username)
        if not user:
            return jsonify({
                "status": False,
                "message": "Invalid Credentials"
            })

        if not Auth._verify_password(password, user):
            return jsonify({
                "status": False,
                "message": "Invalid Credentials"
            })

        token = Auth._generate_token({"username": user.username, "id": user.get_id})
        return jsonify({
            "status": True,
            "token": token
        })
