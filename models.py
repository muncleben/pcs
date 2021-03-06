import datetime

from werkzeug.security import generate_password_hash, check_password_hash

from exts import db


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    phone = db.Column(db.String(11), nullable = False)
    username = db.Column(db.String(18), nullable = False)
    password = db.Column(db.String(100), nullable = False)

    def __init__(self, *args, **kwargs):
        phone = kwargs.get('phone')
        username = kwargs.get('username')
        password = kwargs.get('password')

        self.phone = phone
        self.username = username
        self.password = generate_password_hash(password)

    def check_password(self, input_password):
        pwd_check_result = check_password_hash(self.password, input_password)
        return pwd_check_result


class Prescription(db.Model):
    __tablename__ = 'prescription'
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    t_id = db.Column(db.String(11), nullable=False)
    name = db.Column(db.String(18), nullable=False)
    gender = db.Column(db.String(2), nullable=False)
    age = db.Column(db.String(3), nullable=False)
    pre_date = db.Column(db.DateTime)
    diagnosis = db.Column(db.Text, nullable=False)
    first_page = db.Column(db.String(2), nullable=False)
    second_page = db.Column(db.String(2), nullable=False)
    third_page = db.Column(db.String(2), nullable=False)
    injection = db.Column(db.String(2), nullable=False)
    pre_amount = db.Column(db.Float(2), nullable=False)
    prescriber = db.Column(db.String(18), nullable=False)
    section = db.Column(db.String(36), nullable=False)
    reasonable = db.Column(db.String(2), nullable=False)
    comments = db.Column(db.Text)
