from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
#from werkzeug import generate_password_hash, check_password_hash
#c:/Users/Frale/Flask/env/Scripts/activate.bat activate environment

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

"""class User(db.Model): #Code for the users database
    __tablename__ = 'users'
    uid = db.Column(db.Integer, primary_key =True)
    firstname = db.Column(db.string(100))
    lastname = db.Column(db.string(100))
    email = db.Column(db.String(120), unique=True)
    pwdhash = db.Column(db.String(54))"""

class Todo(db.Model): #code given from the tutorial
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    completed = db.Column(db.Integer, default=0)
    date_created = db.Column(db.DateTime, default= datetime.utcnow)

    def __repr__(self):
        return '<Task %r>' % self.id

@app.route('/')
def index():
    return render_template('index.html')
    

if __name__ == "__main__":
    app.run(debug=True)
    