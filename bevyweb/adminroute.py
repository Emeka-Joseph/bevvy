import os,random, time,string

from flask import render_template, redirect, flash, session, request, url_for
from sqlalchemy import desc,asc,or_,func
from bevyweb.models import Messages,Sessions,Login,Album
from bevyweb import app,db


def generate_name(): 
    filename = random.sample(string.ascii_lowercase,10) 
    return ''.join(filename) 

@app.route('/admin', methods=['POST','GET'])
def admin_home():
    id = session.get('admin')
    if id==None:
        return redirect(url_for('admin_login'))
    else:
        booked_session= db.session.query(Sessions).all()
        return render_template('admin/admin_index.html', booked_session=booked_session)


@app.route('/admin/messages',methods=['POST','GET'])
def admin_messages():
    id = session.get('admin')
    if id==None:
        return redirect(url_for('admin_login'))
    else:
        messages = db.session.query(Messages).all()
        return render_template('admin/messages.html',messages=messages)
    
@app.route('/admin/gallery',methods=['POST','GET'])
def admin_gallery():
    id = session.get('admin')
    if id==None:
        return redirect(url_for('admin_login'))
    else:
        propic = Album.query.order_by(Album.album_id.desc()).all()
        return render_template('admin/gallery.html',propic=propic)
    

@app.route('/admin/login')
def log():
    return render_template('admin/login.html')

@app.route('/login', methods=['GET','POST'])
def admin_login():
    if request.method=='GET':
        return render_template('admin/login.html')
    else:
        email=request.form.get('admin_mail')
        pwd=request.form.get('password') 
        deets = db.session.query(Login).filter(Login.email_address==email).first() 
        passdeets = db.session.query(Login).filter(Login.password).first()
        if deets !=None and passdeets !=None:
            id = deets.admin_id
            session['admin'] = id
            return redirect(url_for('admin_home'))
        else:
            flash('Invalid email or password')
            return redirect(url_for('admin_login'))

@app.route('/album', methods=['POST', 'GET'])
def album():
    id = session.get('admin')
    if id ==None:
        return render_template('admin/login.html')
    else:
        if request.method =='GET':
            deets = db.session.query(Login).filter(Login.admin_id==id).first()
            adeets = db.session.query(Album.album_name).first()

            propic = Album.query.order_by(Album.album_id.desc()).all()

            pics = request.files
            return render_template('admin/gallery.html',deets=deets,adeets=adeets,propic=propic)
        else:
            pics = request.files['gallery']  
            filename = pics.filename
            filetype = pics.mimetype
            allowed = ['.png','.PNG', '.jpg','JPG', '.jpeg','.JPEG','.mp4']
            if filename !='':
                name,ext = os.path.splitext(filename) 
                if ext.lower() in allowed:
                    newname = generate_name()+ext
                    pics.save("bevyweb/static/uploads/"+newname)
                    #albumobj = db.session.query(Users).get(session['user'])
                    #albumid = db.session.query(Login).get(session['admin'])
                    #albumid.user_album.Album_userid=id

                    #albumid.user_id=session['user']
                    f = Album(album_name=newname) 
                    db.session.add(f)
                    db.session.commit()
                    flash('File uploaded successfully')
                    return redirect(url_for('admin_home'))
                else:
                    return 'File extension not allowed '
            else:
                flash('Please chose a file')

@app.route('/delete/<int:id>')
def delete(id): 
    pic_to_del=Album.query.get_or_404(id)
    try:
        db.session.delete(pic_to_del)
        db.session.commit()
        flash('Picture deleted successfully') 
        return redirect(url_for('album'))
        
    except:
        flash('whoops, there was a problem deleting the picutre')
        return redirect(url_for('user_dashboard'))


@app.route('/logout')
def admin_logout():
    #pop the session redirect to home page
    #adminlog = db.session.query(Login).all()
    if session.get('admin')!=None:
        session.pop('admin',None)
    return redirect(url_for('admin_login'))