# app/routes.py
from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify,current_app
from .extensions import db
from .models import User, Message,PropertyListing, Photos
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename
from flask_login import login_user, login_required, current_user
from flask import jsonify
from sqlalchemy import func, case
import os


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

# @main_bp.route('/create_property_listing', methods=['POST'])
# @login_required
# def create_property_listing():
#     #use request.form to access form data
#     title = request.form.get('title')
#     description = request.form.get('description')
#     price = request.form.get('price')
#     location = request.form.get('location')
#     user_id = 1

#     # Convert price to an integer
#     try:
#         price = int(price)
#     except ValueError:
#         flash('Price must be a number.')
#         return redirect(url_for('main.admin_dashboard.'))
    
#     new_property = PropertyListing(title=title, description=description, price=price, location=location)
   
#     db.session.add(new_property)
#     db.session.commit()

#     flash('Property listing created successfully.')
#     return redirect(url_for('main.admin_dashboard'))
###############################################################################################
# ALLOWED_EXTENSIONS = {'jpg', 'jpeg', 'png'}
# def allowed_file(filename):
#     return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# @main_bp.route('/create_property_listing', methods=['POST'])
# @login_required
# def create_property_listing():
#     if 'image' not in request.files:
#         flash('No image part')
#         return redirect(request.url)
#     image = request.files['image']
#     if image.filename == '':
#         flash('No image selected for uploading')
#         return redirect(request.url)
    
#     # Validate and save the image
#     if image and allowed_file(image.filename):
#         filename = secure_filename(image.filename)
#         image_path = os.path.join(current_app.config['UPLOAD_FOLDER'], filename)
#         image.save(image_path)
#     else:
#         flash('Allowed image types are -> jpg, jpeg, png')
#         return redirect(request.url)

#     title = request.form.get('title')
#     description = request.form.get('description')
#     price = request.form.get('price')
#     location = request.form.get('location')

#     # Convert price to an integer
#     try:
#         price = int(price)
#     except ValueError:
#         flash('Price must be a number.')
#         return redirect(url_for('main.admin_dashboard'))
    
#     # Save the new property listing with the image
#     new_property = PropertyListing(title=title, description=description, price=price, location=location)
#     db.session.add(new_property)
#     db.session.commit()

#     flash('Property listing created successfully.')
#     return redirect(url_for('main.admin_dashboard'))
#######################################################################
# ALLOWED_EXTENSIONS = {'jpg', 'jpeg', 'png'}

# def allowed_file(filename):
#     return '.' in filename and \
#            filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


# @main_bp.route('/create_property_listing', methods=['POST'])
# @login_required
# def create_property_listing():
#     title = request.form.get('title')
#     description = request.form.get('description')
#     price = request.form.get('price')
#     location = request.form.get('location')

#     try:
#         price = int(price)
#     except ValueError:
#         flash('Price must be a number.')
#         return redirect(url_for('main.admin_dashboard'))
    
#     # Create the new property listing
#     new_property = PropertyListing(title=title, description=description, price=price, location=location)
#     db.session.add(new_property)
    
#     images = request.files.getlist('images')
#     for image in images:
#         if image and allowed_file(image.filename):
#             filename = secure_filename(image.filename)
#             image_path = os.path.join(current_app.config['UPLOAD_FOLDER'], filename)
#             image.save(image_path)
#             # Create a new Photo instance for each image
#             new_photo = Photos(photo=filename, property=new_property)
#             db.session.add(new_photo)
#         else:
#             flash('Some images were not saved. Allowed image types are -> jpg, jpeg, png')
    
#     db.session.commit()

#     flash('Property listing and associated images uploaded successfully.')
#     return redirect(url_for('main.admin_dashboard'))

# Helper function to check allowed file extensions
ALLOWED_EXTENSIONS = {'jpg', 'jpeg', 'png'}
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@main_bp.route('/create_property_listing', methods=['POST'])
@login_required
def create_property_listing():
    if request.method == 'POST':
        if 'images' not in request.files:
            flash('No images part')
            return redirect(request.url)
        
        images = request.files.getlist('images')
        
        if not images or any(image.filename == '' for image in images):
            flash('No image selected for uploading')
            return redirect(request.url)
        
        uploaded_filenames = []
        for image in images:
            if image and allowed_file(image.filename):
                filename = secure_filename(image.filename)
                image_path = os.path.join(current_app.config['UPLOAD_FOLDER'], filename)
                image.save(image_path)
                uploaded_filenames.append(filename)
            else:
                flash('Allowed image types are -> jpg, jpeg, png')
                return redirect(request.url)
        
        # Form data
        title = request.form.get('title')
        description = request.form.get('description')
        price = request.form.get('price')
        location = request.form.get('location')
        
        # Save the new property listing
        try:
            price = int(price)
        except ValueError:
            flash('Price must be a number.')
            return redirect(url_for('main.admin_dashboard'))
        
        new_property = PropertyListing(title=title, description=description, price=price, location=location)
        db.session.add(new_property)
        db.session.flush()  # This is used to get the id of the new_property before committing

        # Associate uploaded images with this property
        for filename in uploaded_filenames:
            new_photo = Photos(photo=filename, property_id=new_property.id)
            db.session.add(new_photo)
        
        db.session.commit()
        flash('Property listing created successfully.')
        
        return redirect(url_for('main.admin_dashboard'))
#######################################################################

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



