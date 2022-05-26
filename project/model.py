
from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
class User(db.Model,UserMixin):
    
     name = db.Column(db.String(20), nullable=False) 
     phone= db.Column(db.Integer, primary_key=True)
     password=db.Column(db.String(15),nullable=False)
     con_password=db.Column(db.String(15),nullable=False)
     email = db.Column(db.String(40), nullable=False)
     address=db.Column(db.String(255),nullable=False)
     def __repr__(self):
        return '<User %r>' % self.username
class student(db.Model):
     Email = db.Column(db.String(120),primary_key=True ,nullable=False)
     Password=db.Column(db.String(123),nullable=False)
     def __repr__(self):
        return '<User %r>' % self.username

class Product(db.Model):
   id=db.Column(db.Integer,primary_key = True)
   courses = db.Column(db.Text,nullable = False)
   duration = db.Column(db.Text,nullable = False)
   fee = db.Column(db.Integer,nullable = False)
   disc= db.Column(db.Text,nullable = False)
   image=db.Column(db.Text, nullable =False)
   filename=db.Column(db.Text)
   mimetype = db.Column(db.Text,nullable = False)
   
    

   def __init__(self,courses,duration,fee,disc,image,date,mimetype,filename=filename):
      self.courses = courses
      self.duration = duration
      self.fee = fee
      self.disc = disc
      self.image = image
      self.date = date
      self.mimetype = mimetype
      self.filename = filename