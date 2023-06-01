from datetime import datetime
from bevyweb import db 


class Users(db.Model):
    user_id = db.Column(db.Integer, autoincrement=True,primary_key=True)
    user_fullname = db.Column(db.String(100),nullable=False)
    user_phone=db.Column(db.String(120),nullable=False) 
    user_email = db.Column(db.String(120), nullable=False, unique=True)
