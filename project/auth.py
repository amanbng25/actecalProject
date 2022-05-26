from flask import Flask, Response, redirect, url_for, request, session, abort, g,render_template, flash
from flask_login import LoginManager, UserMixin, login_required, login_user, logout_user, current_user
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import PrimaryKeyConstraint
from project.model import User,Product
from datetime import timedelta
from flask import Blueprint
from project import db
from werkzeug.utils import secure_filename
import os

auth = Blueprint('auth', __name__)

Upload_Folder = "project/static/pictures"




@auth.route("/logout")
def logout():
   
   

   
    return redirect("/")

@auth.route('/studentdata')
def studentdata():
  return render_template("studentdata.html")

@auth.route('/studentlogin')
def studentLoginForm():
  return render_template("studentlogin.html")





 

@auth.before_request
def before_request():
  session.permanent= True
  auth.permanent_session_lifetime=timedelta(minutes=1)
  session.modified= True
  g.user = current_user


@auth.route('/addany',methods=['POST'])
@login_required
def addany():
    pic = request.files["pic"]
    if not pic:
      return 'no pic uploaded'
    
    courses= request.form.get('courses')
    pic_name = secure_filename(pic.filename)
    mimetype = pic.mimetype
    duration= request.form.get('duration')
    fee= request.form.get('fee')
    disc= request.form.get('disc')

    if not pic_name or not mimetype:
      return 'bad upload',400
    pic.save(os.path.join(Upload_Folder, pic_name))

    file_path ='./static/pictures/+pic_name'
    product=Product(courses=courses,duration=duration,fee=fee,disc=disc,image=file_path, mimetype=mimetype,filename=pic_name)
    db.session.add(product)
    db.session.commit()
    product_det= Product.query.all()
    return render_template('gallery.html')

#     @main.route('/adminadddata',methods = ['POST', 'GET'])
# def register():  
#     if request.method=="POST":
#       course=request.form['course']    
#       duration=request.form['duration']  
#       fee=request.form['fee']
#       desc=request.form['desc'] 
       
     
      
#     else:
#         return render_template("register.html")
#     data=Product(courses=courses,duration=duration,fee=fee,desc=desc)
#     db.session.add(data)  # Adds new User record to database
#     db.session.commit()  # Commits all changes
#     return render_template("studentdata.html", data=Product.query.all())