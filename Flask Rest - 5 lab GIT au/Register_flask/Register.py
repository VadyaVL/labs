from flask import Flask
from flask import render_template
from flask_sqlalchemy import SQLAlchemy
from flask_restless import *
import os

app = Flask(__name__)
#app.config.update(SERVER_NAME='localhost:5010')
DB_PATH = 'sqlite:///' + os.path.dirname(os.path.abspath(__file__)) + '/register.db'
#DB_PATH = 'sqlite:///' + os.path.dirname(os.path.abspath(__file__)) + '/SQLite.db'

app.config['SQLALCHEMY_DATABASE_URI'] = DB_PATH  # 'sqlite:////tmp/register.db'
db = SQLAlchemy(app)

class Object(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(45), unique=True)
    serial = db.Column(db.String(45), unique=True)
    encs = db.relationship('Encumbrance', backref='object',
                                lazy='dynamic')

class Address(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    country = db.Column(db.String(200), unique=True)
    city = db.Column(db.String(200), unique=True)
    street = db.Column(db.String(200), unique=True)
    persons = db.relationship('Person', backref='address',
                                lazy='dynamic')

class Type(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), unique=True)
    encs = db.relationship('Encumbrance', backref='type',
                                lazy='dynamic')

class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    identification = db.Column(db.String(10), unique=True)
    name = db.Column(db.String(200), unique=True)
    address_id = db.Column(db.Integer, db.ForeignKey('address.id'))
    encs = db.relationship('Encumbrance', backref='person',
                                lazy='dynamic')

class Encumbrance(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    numberStatement = db.Column(db.String(10), unique=True)
    dateStatement = db.Column(db.Date)
    type_id = db.Column(db.Integer, db.ForeignKey('type.id'))
    object_id = db.Column(db.Integer, db.ForeignKey('object.id'))
    person_id = db.Column(db.Integer, db.ForeignKey('person.id'))


@app.route('/')
def index():
    return render_template('Index.html')

if __name__ == '__main__':

    mr_manager = APIManager(app, flask_sqlalchemy_db=db)
    mr_manager.create_api(Object, methods=['GET', 'POST'])# , exclude_columns=['methods'])
    mr_manager.create_api(Address, methods=['GET', 'POST'])# , include_columns=['id', 'name', 'methods', 'methods.name'])
    mr_manager.create_api(Type, methods=['GET', 'POST', 'PATCH', 'DELETE'])
    mr_manager.create_api(Person, methods=['GET', 'POST'])
    mr_manager.create_api(Encumbrance, methods=['GET', 'POST','PATCH' ,  'DELETE'])#,
                          # include_columns=['id', 'name', 'authors', 'authors.name', 'category', 'category.name',
                          #                  'creation_date', 'approval_date'])
    app.run(host='127.0.0.1', port=5010)
    # print(DB_PATH)