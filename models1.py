from flask_login import UserMixin
from app2 import db

class User(UserMixin,db.Model):
    __tablename__ = 'users'

    uid = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(80),nullable=False)
    password = db.Column(db.String(255),nullable=False)
    role = db.Column(db.String(80))
    description = db.Column(db.String(500))

    def get_id(self):
        return str(self.uid)

    def __repr__(self):
        return f'<User: {self.username},Role: {self.role}>'

    