
from flask_sqlalchemy import SQLAlchemy
from geoalchemy2 import Geometry

db = SQLAlchemy()

class Building(db.Model):
    __tablename__ = "building"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    geometry = db.Column(Geometry('POLYGON'))

class Road(db.Model):
    __tablename__ = "road"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    geometry = db.Column(Geometry('LINESTRING'))
