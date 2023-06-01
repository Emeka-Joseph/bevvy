import os,random, time

from flask import render_template, redirect, flash, session, request, url_for

from bevyweb import app,db



@app.route('/')
def home():
    return render_template('users/index.html')

@app.route('/about')
def about():
    return render_template('users/about.html')


@app.route('/gallery')
def gallery():
    return render_template('users/gallery.html')


@app.route('/book_session')
def book_session():
    return render_template('users/session.html')

