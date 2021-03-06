from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, Float
import os
app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'planets.db')

db = SQLAlchemy(app)

@app.cli.command
def db_create():
    db.create_all()
    print("Database Created!")

@app.cli.command
def db_drop():
    db.drop_all()
    print("Database Dropped!")

@app.cli.command
def seed():
    mercury = Planet(planet_name='Mercury',
                     planet_type='Class D',
                     home_star='Sol',
                     mass=2.258e23,
                     radius=1516,
                     distance=35.98e6)

    venus = Planet(planet_name='Venus',
                         planet_type='Class K',
                         home_star='Sol',
                         mass=4.867e24,
                         radius=3760,
                         distance=67.24e6)

    earth = Planet(planet_name='Earth',
                     planet_type='Class M',
                     home_star='Sol',
                     mass=5.972e24,
                     radius=3959,
                     distance=92.96e6)

    db.session.add(mercury)
    db.session.add(venus)
    db.session.add(earth)

    test_user = User(first_name='William',
                     last_name='Herschel',
                     email='test@test.com',
                     password='P@ssw0rd')

    db.session.add(test_user)
    db.session.commit()
    print("Database Seeded!")

@app.route('/')
def hello_world():
    return jsonify('Hello World!'), 200

@app.route('/super_simple')
def super_simple():
    return jsonify(message="Simple Life!")

@app.route('/not_found')
def not_found():
    return jsonify(message="Not found"), 404

@app.route('/parameters')
def parameters():
    name= request.args.get('name')
    age = int(request.args.get('age'))
    if age < 18:
        return jsonify(message = "Sorry " + name + " you are not old enough"), 401
    else:
        return jsonify(message = "Welcome " + name + " you are old enough"), 200

# localhost:5000/url_variables/name/age
@app.route('/url_variables/<string:name>/<int:age>')
def url_variables(name: str, age: int):
    if age < 18:
        return jsonify(message = "Sorry " + name + " you are not old enough"), 401
    else:
        return jsonify(message = "Welcome " + name + " you are old enough"), 200

# Database
class User(db.Model):
    __tablename__= 'users'
    id = Column(Integer, primary_key=True)
    first_name=Column(String)
    last_name=Column(String)
    email=Column(String, unique=True)
    password=Column(String)

class Planet(db.Model):
    __tablename__= 'planets'
    planet_id=Column(String, primary_key=True)
    planet_naem=Column(String)
    planet_type=Column(String)
    home_star=Column(String)
    mass=Column(Float)
    radius=Column(Float)
    distance=Column(Float)

if __name__ == '__main__':
    app.run()
