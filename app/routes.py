# app/routes.py
from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify
from .extensions import db
from .models import User, Message,PropertyListing
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, current_user
from flask import jsonify
from sqlalchemy import func, case


main_bp = Blueprint('main', __name__)


@main_bp.route('/', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('password')
        
        # Check if user already exists
        user = User.query.filter_by(email=email).first()
        if user:
            flash('Email already registered.')
            return redirect(url_for('main.register'))
        
        # Create new user with hashed password
        hashed_password = generate_password_hash(password)
        new_user = User(name=name, email=email, password_hash=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        
        flash('Registration successful! Please login.')
        return redirect(url_for('main.login'))
    
    return render_template('register.html')


# Here is the code for the login route.

@main_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        user = User.query.filter_by(email=email).first()

        if user and check_password_hash(user.password_hash, password):
            login_user(user)
            if user.is_admin:
                return redirect(url_for('main.admin_dashboard'))
            else:  # This else should align with if user.is_admin
                return redirect(url_for('main.user_messages'))
        else:
            flash('Invalid email or password.')  # Provide feedback for failed login

    return render_template('login.html')

# Here we will start working on the messaging feature. We will create two routes: one for the user and one for the admin.

@main_bp.route('/send_message', methods=['POST'])
@login_required
def send_message():
  data = request.get_json()
  content = data.get('content')
  # Assuming the recipient_id for the owner/admin is known, e.g., 1
  # and 'current_user' is the sender who is logged in
  new_message = Message(sender_id=current_user.id, recipient_id=1, content=content)

  # Save the new message to the database
  db.session.add(new_message)
  db.session.commit()

  return jsonify({'message': 'Message sent successfully', 'content': content})

@main_bp.route('/get_my_conversation_with_owner')
@login_required
def get_my_conversation_with_owner():
    # Fetch messages where the current user is either the sender or recipient
    messages = Message.query.filter(
        (Message.sender_id == current_user.id) | 
        (Message.recipient_id == current_user.id)
    ).order_by(Message.timestamp.asc()).all()

    # Transform the messages into a JSON-serializable format
    messages_data = [{
        'id': message.id,
        'sender_id': message.sender_id,
        'recipient_id': message.recipient_id,
        'content': message.content,
        'timestamp': message.timestamp.strftime('%Y-%m-%d %H:%M:%S'),
        'read': message.read
    } for message in messages]

    return jsonify(messages=messages_data)



# Here is the code for the admin route.###################################################
@main_bp.route('/get_user_list')
@login_required
def get_user_list():
    if not current_user.is_admin:
        # Ensure only admin users can access this route
        return jsonify({'error': 'Unauthorized'}), 403

    # Example: Fetching user IDs and names who have sent messages
    user_list_query = db.session.query(
        Message.sender_id,
        User.name
    ).join(User, User.id == Message.sender_id).distinct()

    user_list = [{'sender_id': user.sender_id, 'name': user.name} for user in user_list_query.all()]

    return jsonify({'user_list': user_list})

#################################################################### for viewing client messages
@main_bp.route('/admin_messages/<int:user_id>')
@login_required
def admin_messages(user_id):
    if not current_user.is_admin:
        return jsonify({'error': 'Unauthorized'}), 403

    user = User.query.get(user_id)
    messages = Message.query.filter(
        (Message.sender_id == user_id) & (Message.recipient_id == current_user.id) | 
        (Message.sender_id == current_user.id) & (Message.recipient_id == user_id)
    ).order_by(Message.timestamp.asc()).all()

    return render_template('admin_messages.html', user=user, messages=messages)

#################################################################### for sending client messages
@main_bp.route('/send_message_to_user/<int:user_id>', methods=['POST'])
@login_required
def send_message_to_user(user_id):
    if not current_user.is_admin:
        return jsonify({'error': 'Unauthorized'}), 403

    data = request.json
    new_message = Message(sender_id=current_user.id, recipient_id=user_id, content=data['content'])
    db.session.add(new_message)
    db.session.commit()

    return jsonify({'message': 'Message sent successfully'})

#################################################################### for creating a new property listing

@main_bp.route('/create_property_listing', methods=['POST'])
@login_required
def create_property_listing():
    #use request.form to access form data
    title = request.form.get('title')
    description = request.form.get('description')
    price = request.form.get('price')
    location = request.form.get('location')

    # Convert price to an integer
    try:
        price = int(price)
    except ValueError:
        flash('Price must be a number.')
        return redirect(url_for('main.admin_dashboard.'))
    
    new_property = PropertyListing(title=title, description=description, price=price, location=location)
   
    db.session.add(new_property)
    db.session.commit()

    flash('Property listing created successfully.')
    return redirect(url_for('main.admin_dashboard'))


@main_bp.route('/index')
def index():
    return render_template('index.html')

@main_bp.route('/user_messages')
@login_required
def user_messages():
    # Ensure only non-admin users can access this page
    if current_user.is_admin:
        return redirect(url_for('main.index'))  # or some other appropriate action
    return render_template('user_messages.html')

@main_bp.route('/admin_dashboard')
@login_required
def admin_dashboard():
    # Ensure only admin users can access this page
    if not current_user.is_admin:
        return redirect(url_for('main.index'))  # or some appropriate action
    return render_template('admin_dashboard.html')



