from flask import Flask
from flask_sqlalchemy import SQLAlchemy

serv = Flask(__name__)
serv.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:siscov@localhost:5432/teste'
serv.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(serv)

class Estado(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)

    def __init__(self, name):
        self.name = name