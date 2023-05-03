from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from flask_sqlalchemy import SQLAlchemy
import time
from app import db

class User(db.Model):
    id = Column(db.Integer, primary_key=True, index=True)
    username = db.Column(db.String(100))
    password = db.Column(db.String(100))
    createdAt = db.Column(db.Integer, default=time.time()) # unix time format
    updateAt = db.Column(db.Integer, default=time.time()) # unix time format


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True, index=True)
    title = db.Column(db.String(100))
    image = db.Column(db.String(200))
    price = db.Column(db.Integer)
    desc = db.Column(db.String(100))
    stock = db.Column(db.Integer)
    createdAt = db.Column(db.Integer, default=time.time()) # unix time format
    updateAt = db.Column(db.Integer, default=time.time()) # unix time format