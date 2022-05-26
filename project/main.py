from distutils.command.upload import upload
from flask import Blueprint
from flask import Flask, Response, redirect, url_for, request, session, abort, g,render_template
from flask_login import login_required
from . import db
from .model import User,Product
from flask_session import Session

import os

main = Blueprint('main', __name__)

Upload_Folder = "project/static/pictures"



@main.route('/')
def home():
  
#  if not session.get("name"):
#         # if not there in the session then redirect to the login page
#         return redirect("/studentlogin")
 return render_template('home.html')


@main.route('/register',methods = ['POST', 'GET'])
def register():  
    if request.method=="POST":
      name=request.form['name']    
      phone=request.form['phone']  
      password=request.form['password']
      con_password=request.form['con_password'] 
      email=request.form['email'] 
      address=request.form['address'] 
     
      
    else:
        return render_template("register.html")
    data=User(name=name,phone=phone,password=password,con_password=con_password,email=email,address=address)
    db.session.add(data)  # Adds new User record to database
    db.session.commit()  # Commits all changes
    return render_template("home.html", data=User.query.all())

@main.route('/studentlogin',methods = ['POST'])
def studentlogin():
  session.permanent = True
  if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]
        session["email"] = request.form.get('email')
        
        login = User.query.filter_by(email=email, password=password).first()
        if login is not None:
            return render_template("home.html",user=User.query.all())
  return render_template("studentlogin.html")


@main.route('/ourcourses')
def ourcourses():
  return render_template("ourcourses.html")


# @main.route('/adminadddata',methods = ['POST', 'GET'])
# def reg():  
#     if request.method=="POST":
#       courses=request.form['courses']    
#       duration=request.form['duration']  
#       fee=request.form['fee']
#       desc=request.form['desc'] 
       
     
      
#     else:
#         return render_template("register.html")
#     data=Product(courses=courses,duration=duration,fee=fee,desc=desc)
#     db.session.add(data)  # Adds new User record to database
#     db.session.commit()  # Commits all changes
#     return render_template("studentdata.html", data=Product.query.all())



