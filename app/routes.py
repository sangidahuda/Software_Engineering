"""
routes.py

This file is the traffic controller of our application. It listens for requests from users 
(like clicking a link or submitting a form) and then tells the application how to respond. 
For each route (URL path), we define a function that creates the page the user sees. 
These functions can pull information from our database, use it to fill out templates, or accept 
user input to create new records in our database.
"""
from flask import Flask, render_template, request, redirect, url_for, flash
import models
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from sqlalchemy import ForeignKey
from app import db


app = Flask(__name__)



@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form.get('name')
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        
        # Check if email already exists
        user = models.User.query.filter_by(email=email).first()
        if user:
            flash('Email already exists.')
            return redirect(url_for('register'))
        # Assign password directly without hashing
        new_user = models.User(name=name, username=username, email=email, password=password)
        db.session.add(new_user)
        db.session.commit()
        # Redirect or log in the user
        return redirect(url_for('login'))
    return render_template('register.html')

# Work from Dyland

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        
        # Check if email and password match the database entry
        user = models.User.query.filter_by(email=email).first()
        if user and user.password == password:
            # For the demo, we'll just redirect to a dummy home page on successful login
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check email and password')
            return redirect(url_for('login'))
    return render_template('login.html')


@app.route('/send_message', methods=['POST'])
def send_message():
   if request.method == 'POST':
       sender_id = request.form.get('sender_id')
       recipient_id = request.form.get('recipient_id')
       content = request.form.get('content')
        
        # Create a new message instance
       new_message = models.Message(sender_id=sender_id, recipient_id=recipient_id, content=content)
       db.session.add(new_message)
       db.session.commit()
        
       flash('Message sent successfully!')
       return redirect(url_for('home'))  # Adjust the redirect as needed
   else:
        # Optionally handle GET request or redirect
       return redirect(url_for('send_message_form'))

@app.route('/view_messages/<int:user_id>')
def view_messages(user_id):
    # Assuming 'user_id' is the ID of the recipient
   received_messages = models.Message.query.filter_by(recipient_id=user_id).order_by(models.Message.created_at.desc()).all()
   return render_template('view_messages.html', messages=received_messages)


