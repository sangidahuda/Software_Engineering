"""
models.py

This module serves as our application's database schema defined using SQLAlchemy ORM. 
Using SQLAlchemy allows us to define our database structure with Python classes, making the process
more intuitive and pythonic compared to writing raw SQL. This approach not only speeds up development 
but also enhances code readability and maintainability. It abstracts complex SQL queries into simple 
Python methods, thereby reducing the risk of SQL injection attacks and making our application more secure. 

We define tables as classes and columns as class attributes, with relationships between tables managed through 
foreign keys. This setup is directly influenced by our ER diagram, ensuring our database schema accurately 
reflects the intended data model. Familiarity with SQL will still be beneficial, as it underpins how SQLAlchemy 
operates, providing a solid foundation for understanding and optimizing database interactions.
"""
# models.py
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from app import db

# Define the User model, inheriting from UserMixin for Flask-Login integration
class User(UserMixin, db.Model):
    # User's database table columns
    id = db.Column(db.Integer, primary_key=True)  # Unique identifier for each user
    name = db.Column(db.String(100), nullable=False)  # User's name
    email = db.Column(db.String(100), unique=True, nullable=False)  # User's email, must be unique
    password = db.Column(db.String(200), nullable=False)  # Hashed password
    is_admin = db.Column(db.Boolean, default=False)  # Flag to identify admin users

    # Relationship to messages sent by this user
    messages_sent = db.relationship('Message', foreign_keys='Message.sender_id', backref='sender', lazy='dynamic')
    # Relationship to messages received by this user
    messages_received = db.relationship('Message', foreign_keys='Message.recipient_id', backref='recipient', lazy='dynamic')

    def set_password(self, password):
        """Create hashed password."""
        self.password = generate_password_hash(password)

    def check_password(self, password):
        """Check hashed password."""
        return check_password_hash(self.password, password)

# Define the Message model
class Message(db.Model):
    # Message's database table columns
    id = db.Column(db.Integer, primary_key=True)  # Unique identifier for each message
    sender_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)  # User ID of the message sender
    recipient_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)  # User ID of the message recipient
    content = db.Column(db.String(1000), nullable=False)  # Content of the message
    created_at = db.Column(db.DateTime, index=True, default=datetime.utcnow)  # Timestamp of when the message was sent
    read = db.Column(db.Boolean, default=False)  # Flag to track if the message has been read

# Note: Ensure you have imported db from your Flask app instance, usually defined in your app's __init__.py file:
# from app import db


class Property(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    price = db.Column(db.Integer, nullable=False)
    location = db.Column(db.String(100), nullable=False)
    images = db.relationship('PropertyImage', backref='property', lazy=True)
    

class PropertyImage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    property_id = db.Column(db.Integer, db.ForeignKey('property.id'), nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')    

class reservation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    property_id = db.Column(db.Integer, db.ForeignKey('property.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    start_date = db.Column(db.DateTime, nullable=False)
    end_date = db.Column(db.DateTime, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow)

class Payment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    reservation_id = db.Column(db.Integer, db.ForeignKey('reservation.id'), nullable=False)
    amount = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow)




    

