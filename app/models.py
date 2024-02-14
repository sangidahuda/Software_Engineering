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
# Rest of the code follows, defining tables and their relationships...


#First we start of creating a user object which will contain Name, Username ,Email, Password and Profile Picture

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    posts = db.relationship('Post', backref='author', lazy=True)


    #

