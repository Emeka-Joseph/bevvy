import os,random, time

from flask import render_template, redirect, flash, session, request, url_for
from bevyweb.models import Messages,Sessions,Album
from bevyweb import app,db



@app.route('/')
def home():
    return render_template('users/index.html')

@app.route('/about')
def about():
    return render_template('users/about.html')


@app.route('/gallery')
def gallery():
    #propic = db.session.query(Album).all()
    propic = Album.query.order_by(Album.album_id.desc()).all()
    return render_template('users/gallery.html',propic=propic)


@app.route('/book_session', methods=['GET','POST'])
def book_session():
    if request.method=='GET':
        return render_template('users/session.html')
    else:
        name = request.form.get('client_name')
        mail = request.form.get('client_mail')
        phone = request.form.get('client_phone')
        shoot = request.form.get('shoot')
        space = request.form.get('space')
        edit = request.form.get('edit')
        book_date = request.form.get('date')
        amount = request.form.get('amount')
        naration = request.form.get('details')

        if mail !='' and name !='' and phone !='' and book_date !='':
            s = Sessions(name=name,email=mail,phone=phone,photo_shoot=shoot,space=space,editing=edit,date=book_date,amount_paid=amount,naration=naration)
            db.session.add(s)
            db.session.commit()
            flash('Your booking has been received and noted, we expect to see you as soon')
            return redirect(url_for('book_session'))
        else:
            flash('Make sure that the filds were rightly filled')

        



@app.route('/messages', methods=['GET','POST'])
def messages():
    if request.method=='GET':
        return render_template('users/index.html')
    else: 
        mail = request.form.get('mail')
        phone = request.form.get('phone')
        name = request.form.get('name')
        content = request.form.get('message')
        if mail !='' and name !='' and content !='' and phone !='':
            m = Messages(email_address=mail,phone_no=phone,name=name,msg_content=content)
            db.session.add(m)
            db.session.commit()
            flash('Thank you for contacting us, we will attend to your message shortly and respond accordingly')
            return redirect(url_for('home'))
        else:
            flash('Make sure that the filds were rightly filled')


