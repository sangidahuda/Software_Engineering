"""
routes.py

This file is the traffic controller of our application. It listens for requests from users 
(like clicking a link or submitting a form) and then tells the application how to respond. 
For each route (URL path), we define a function that creates the page the user sees. 
These functions can pull information from our database, use it to fill out templates, or accept 
user input to create new records in our database.
"""

# routes.py
from flask import Flask, jsonify, request, redirect, url_for, flash, session
from flask_login import login_user, logout_user, current_user, login_required
from werkzeug.security import generate_password_hash, check_password_hash
from models import User, Message, db

app = Flask(__name__)

# User registration route
@app.route('/register', methods=['POST'])
def register():
    # Extract registration data from the request
    data = request.get_json()
    name = data['name']
    email = data['email']
    password = data['password']

    # Check if a user already exists with the given email
    existing_user = User.query.filter_by(email=email).first()
    if existing_user:
        # If user exists, return an error message
        return jsonify({'error': 'Email already exists'}), 409

    # Hash the password for secure storage
    hashed_password = generate_password_hash(password, method='sha256')
    
    # Create a new user instance and add it to the database
    new_user = User(name=name, email=email, password=hashed_password)
    db.session.add(new_user)
    db.session.commit()

    # Return success message
    return jsonify({'message': 'User created successfully'}), 201

# User login route
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data['email']
    password = data['password']

    # Find user by email
    user = User.query.filter_by(email=email).first()

    # Check if user exists and password is correct
    if user and check_password_hash(user.password, password):
        # Log the user in
        login_user(user)
        return jsonify({'message': 'Logged in successfully'}), 200
    else:
        # If credentials are invalid, return an error message
        return jsonify({'error': 'Invalid credentials'}), 401

# User logout route
@app.route('/logout')
@login_required
def logout():
    # Log out the current user
    logout_user()
    return jsonify({'message': 'Logged out successfully'}), 200

# Route for sending messages
@app.route('/send_message', methods=['POST'])
@login_required
def send_message():
    data = request.get_json()
    content = data['content']
    recipient_id = 1 if not current_user.is_admin else data.get('recipient_id', 1)

    # Create and add new message to the database
    new_message = Message(sender_id=current_user.id, recipient_id=recipient_id, content=content, read=False)
    db.session.add(new_message)
    db.session.commit()

    return jsonify({'message': 'Message sent successfully'}), 200

# Route for users to view their messages with the admin
@app.route('/view_my_messages')
@login_required
def view_my_messages():
    # Fetch all messages involving the current user
    my_messages = Message.query.filter((Message.sender_id == current_user.id) | (Message.recipient_id == current_user.id)).order_by(Message.created_at.desc()).all()

    # Serialize messages for JSON response
    messages_json = [{'id': msg.id, 'sender_id': msg.sender_id, 'recipient_id': msg.recipient_id, 'content': msg.content, 'created_at': msg.created_at.isoformat(), 'read': msg.read} for msg in my_messages]
    return jsonify(messages=messages_json), 200

# Route for admin to view all messages from clients
@app.route('/admin/view_messages', methods=['GET'])
@login_required
def view_admin_messages():
    if not current_user.is_admin:
        return jsonify({'error': 'Unauthorized access'}), 403

    # Admin views all messages sent to them
    messages = Message.query.filter_by(recipient_id=1).order_by(Message.created_at.desc()).all()
    messages_json = [{'id': msg.id, 'sender_id': msg.sender_id, 'content': msg.content, 'created_at': msg.created_at.isoformat(), 'read': msg.read} for msg in messages]
    return jsonify(messages=messages_json), 200

# Route for marking messages as read
@app.route('/mark_message_as_read/<int:message_id>', methods=['POST'])
@login_required
def mark_message_as_read(message_id):
    message = Message.query.get_or_404(message_id)

    # Ensure only the recipient can mark the message as read
    if message.recipient_id != current_user.id:
        return jsonify({'error': 'Unauthorized'}), 403

    # Mark the message as read
    message.read = True
    db.session.commit()

    return jsonify({'message': 'Message marked as read'}), 200

# Set the secret key for session management
app.secret_key = 'your_secret_key_here'
