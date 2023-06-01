import os,random, time

from flask import render_template, redirect, flash, session, request, url_for

from bevyweb import app,db


@app.route('/admin', methods=['POST','GET'])
def admin_home():
    
    return render_template('users/admin_index.html')