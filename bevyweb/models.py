from datetime import datetime
from bevyweb import db 


class Sessions(db.Model):
    id = db.Column(db.Integer, autoincrement=True,primary_key=True)
    name = db.Column(db.String(100),nullable=False)
    phone=db.Column(db.String(15),nullable=False) 
    email = db.Column(db.String(120), nullable=True)
    photo_shoot=db.Column(db.String(15),nullable=True)
    space=db.Column(db.String(120),nullable=True)
    editing=db.Column(db.String(120),nullable=True)
    book_date = db.Column(db.DateTime(),default=datetime.utcnow)
    date = db.Column(db.DateTime())
    amount_paid = db.Column(db.Float)
    naration = db.Column(db.Text,nullable=True)



class Messages(db.Model):
    msg_id = db.Column(db.Integer, autoincrement=True,primary_key=True)
    name = db.Column(db.String(100),nullable=False)
    email_address = db.Column(db.String(100),nullable=False)
    phone_no =db.Column(db.String(15),nullable=True)
    msg_content = db.Column(db.Text,nullable=True)
     

class Login(db.Model):
    admin_id = db.Column(db.Integer, autoincrement=True,primary_key=True)
    email_address = db.Column(db.String(100),nullable=False)
    password =db.Column(db.String(15),nullable=True)

class Album(db.Model):
    album_id=db.Column(db.Integer, autoincrement=True, primary_key=True)
    album_name=db.Column(db.String(100),nullable=True)

