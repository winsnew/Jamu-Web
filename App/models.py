from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from flask_sqlalchemy import SQLAlchemy
import time
from app import db

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True, index=True)
    title = db.Column(db.String(100))
    image = db.Column(db.String(200))
    price1 = db.Column(db.Integer)
    price2 = db.Column(db.Integer)
    desc = db.Column(db.String(100))
    stock = db.Column(db.Integer)
    createdAt = db.Column(db.Integer, default=time.time()) # unix time format
    updateAt = db.Column(db.Integer, default=time.time()) # unix time format


class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True, index=True)
    name = db.Column(db.String(100))
    address = db.Column(db.String(200))
    phone = db.Column(db.Integer)
    total = db.Column(db.Integer)
    createdAt = db.Column(db.Integer, default=time.time()) # unix time format
    order_items = db.relationship('OrderItem', backref='order')


class OrderItem(db.Model):
    id = db.Column(db.Integer, primary_key=True, index=True)
    product_id = db.Column(db.Integer)
    title = db.Column(db.String(100))
    price1 = db.Column(db.Integer)
    price2 = db.Column(db.Integer)
    jumlah = db.Column(db.Integer)
    total = db.Column(db.Integer, default=price2*jumlah)
    keuntungan = db.Column(db.Integer, default=price2*jumlah-price1*jumlah)
    order_id = db.Column(db.Integer, db.ForeignKey('order.id'), nullable=False)