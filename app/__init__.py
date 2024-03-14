# app/__init__.py
from flask import Flask
from .extensions import db, login_manager

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = '874y57843hfek43rsd4r4'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:Manchester10!@localhost/GSG'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


    app.config['UPLOAD_FOLDER'] = '/Users/jorgegonzales/Desktop/WebsiteImages'    

    db.init_app(app)
    login_manager.init_app(app)

    from .models import User  # Import here to avoid circular imports

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    from .routes import main_bp
    app.register_blueprint(main_bp)

    with app.app_context():
        db.create_all()  # Create database tables for our data models

    return app
