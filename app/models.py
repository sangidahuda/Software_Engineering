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
