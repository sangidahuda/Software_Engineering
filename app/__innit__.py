"""
__init__.py

This is the starting block of our Flask application. Here, we create an instance of the Flask app, 
set up configurations (like database details), and initialize extensions (like SQLAlchemy for database 
operations and Flask-Login for user management). We also define our app's routes by importing them, 
making sure the app knows what to do when users visit different URLs. Essentially, this file sets the 
foundation, ensuring all parts of our application work together seamlessly.
"""
# __init__.py

# Import the required modules
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

# Initialize the Flask application
app = Flask(__name__)

# Configure the database URI and track modifications for SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:Manchester10!@localhost/GSG'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database with the app instance
db = SQLAlchemy(app)

# Initialize Flask-Login manager with the app instance
login_manager = LoginManager()
login_manager.init_app(app)

# Define the default view for login (where to go if login is required)
login_manager.login_view = 'login'

# Define the user loader callback for Flask-Login
# This function is used to reload the user object from the user ID stored in the session
@login_manager.user_loader
def load_user(user_id):
    from models import User  # Import here to avoid circular imports
    return User.query.get(int(user_id))

# Import routes after initializing extensions to avoid circular imports
# This import statement is typically placed at the end of the `__init__.py` file
import routes
