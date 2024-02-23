"""
routes.py

This file is the traffic controller of our application. It listens for requests from users 
(like clicking a link or submitting a form) and then tells the application how to respond. 
For each route (URL path), we define a function that creates the page the user sees. 
These functions can pull information from our database, use it to fill out templates, or accept 
user input to create new records in our database.
"""
from flask import Flask, render_template, request, redirect, url_for, flash
from models import User
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from sqlalchemy import ForeignKey

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:Manchester10!@localhost/GSG'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form.get('name')
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        
        # Check if email already exists
        user = User.query.filter_by(email=email).first()
        if user:
            flash('Email already exists.')
            return redirect(url_for('register'))
        # Assign password directly without hashing
        new_user = User(name=name, username=username, email=email, password=password)
        db.session.add(new_user)
        db.session.commit()
        # Redirect or log in the user
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        
        # Check if email and password match the database entry
        user = User.query.filter_by(email=email).first()
        if user and user.password == password:
            # For the demo, we'll just redirect to a dummy home page on successful login
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check email and password')
            return redirect(url_for('login'))
    return render_template('login.html')
