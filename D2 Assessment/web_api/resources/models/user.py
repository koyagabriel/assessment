from .base import BaseDocument
from app import db
from itsdangerous import (TimedJSONWebSignatureSerializer as Serializer)
from werkzeug.security import generate_password_hash, check_password_hash

class User(BaseDocument):
    username = db.StringField(unique=True, required=True)
    password_hash = db.StringField(required=True)


    @property
    def get_username(self):
        return self.username

    @property
    def password(self):
        raise AttributeError('Password is not a readable attribute')

    @classmethod
    def post(cls, params):
        return cls(
            username=params["username"],
            password_hash=generate_password_hash(params['password'])
        ).save()


    @classmethod
    def find_by_username(cls, username):
        user = User.objects(username=username).first()

        if not user: raise None

        return user
