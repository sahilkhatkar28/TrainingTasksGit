from src.config.config import db

class User(db.Model):
    id = db.Column(db.String(36), primary_key=True)
    username = db.Column(db.String(100),unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    role = db.Column(db.String(36), nullable=False, default='user')


class Product(db.Model):
    id = db.Column(db.String(36))
    name = db.Column(db.String(100), unique= True,nullable=False, primary_key=True)
    price = db.Column(db.Float, nullable=False)
    stock = db.Column(db.Integer, nullable=False)


class Order(db.Model):
    id = db.Column(db.String(36), primary_key=True)
    protuct_name = db.Column(db.String(100),db.ForeignKey('product.name'),nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    status = db.Column(db.String(36), nullable=False, default='pending')