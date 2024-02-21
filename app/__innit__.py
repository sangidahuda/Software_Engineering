# In app/__init__.py or config.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:Manchester10!@localhost/GSG'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)




"""
__init__.py

This is the starting block of our Flask application. Here, we create an instance of the Flask app, 
set up configurations (like database details), and initialize extensions (like SQLAlchemy for database 
operations and Flask-Login for user management). We also define our app's routes by importing them, 
making sure the app knows what to do when users visit different URLs. Essentially, this file sets the 
foundation, ensuring all parts of our application work together seamlessly.
"""
