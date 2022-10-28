from datetime import datetime
from todosapp import db
from hashlib import sha256


class ExtraMixin(object):
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

class User(db.Model, ExtraMixin):
    __tablename__ = 'users'
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)

    @classmethod
    def find_user_by_email(cls, email):
        return cls.query.filter_by(email=email).first()


    @classmethod
    def get_all_users(cls):
        return cls.query.all()

    @staticmethod
    def hash_password(password):
        return sha256(password.encode()).hexdigest()


    @staticmethod
    def verify_hash(password, hash):
        return sha256(password.encode()).hexdigest() == hash


class Todo(db.Model, ExtraMixin):
    __tablename__ = 'todos'
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(255), nullable=False)
    due_date = db.Column(db.DateTime, nullable=False)
    complete = db.Column(db.Boolean, default=False)
    created_by = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    @classmethod
    def get_todos(cls):
        return cls.query.all()

    @classmethod
    def get_user_todos(cls, user_id):
        return cls.query.filter_by(created_by=user_id).all()

    @classmethod
    def get_todo_by_id(cls, todo_id):
        return cls.query.filter_by(id=todo_id).first()
        