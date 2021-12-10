from functools import wraps
from flask.helpers import send_file
from flask_mail import Connection, Mail, Message
from flask import Flask, render_template, request, session, escape, redirect, url_for, flash
from werkzeug.security import generate_password_hash, check_password_hash
import os
from flask import send_from_directory
from flask_login import login_required, UserMixin, login_user
import cv2
from flask_bcrypt import Bcrypt
from werkzeug.utils import secure_filename
from flask import Flask,render_template,request,redirect,url_for,make_response,jsonify
from datetime import timedelta
from wtforms import StringField, PasswordField, SubmitField
from wtforms.fields.simple import TextAreaField
from wtforms.validators import InputRequired, Length, ValidationError
from flask_wtf import FlaskForm



app = Flask(__name__)
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'dhuaitac@ulasalle.edu.pe'
app.config['MAIL_PASSWORD'] = '2001africa'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)






@app.route("/index", methods=["GET", "POST"])
def index():
   
   if request.method == 'POST':
      name=request.form["user_name"]
      email=request.form["user_mail"]
      body=request.form["user_message"]
      msg = Message(name, sender = 'dhuaitac@ulasalle.edu.pe', recipients = [email])
      msg.body = body
      mail.send(msg)
      return render_template('example.html')
   return render_template('example.html')

@app.route('/', methods=["GET", "POST"])
def home():
   return render_template('example.html')

if __name__ == '__main__':
   app.run(debug = True)