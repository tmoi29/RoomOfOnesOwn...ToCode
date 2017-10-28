#A ROOM OF ONE'S OWN...TO CODE
#Irene Lam, Tiffany Moi, Carol Pan
#SoftDev pd7
#P00 - Da Art of Storytellin' 

from flask import Flask, render_template, request, session, redirect, flash, url_for
from util import make_table as make

import os, cgi, hashlib

app = Flask (__name__)

#the_username = "user" #Hardcoded username
#the_password = "pwd"  #Hardcoded password
app.secret_key = os.urandom(32)

@app.route("/")
def hello_world():
    '''
    If session has a record of the correct username and password input, the user is logged in
    Otherwise, the login page is displayed
    '''
    make.db_setup()
    if "username" in session.keys():
       return render_template("welcome.html", name = session["username"])
    return render_template("login.html", message = "")

@app.route("/createaccount")
def create_account():
    return render_template("createaccount.html")

@app.route("/auth")
def check_creation():
    user = request.args["username"]
    #if request.args["username"] is unique will do later
    if request.args["password1"] == request.args["password2"]:
        pwd = request.args["password1"]
        unique = make.createAcc(user,pwd)
        if unique:
            flash("Success!")
            return redirect(url_for("hello_world"))
        else:
            flash ("Oops this user already exists")
            return redirect(url_for("create_account"))
    else:
        flash("Passwords do not match :(")
        return redirect(url_for("create_account"))


@app.route("/welcome")
def logged_in():
   input_name = request.args["username"]
   input_pass = request.args["password"]
   hash_object = hashlib.sha224(input_pass)
   hashed_pass = hash_object.hexdigest()
   lookup = make.auth('"' + input_name + '"')
   #Validation process, what went wrong (if anything)?
   if lookup[0]:
      if hashed_pass == lookup[1][0]:
         session["username"] = input_name #Creates a new session
         return render_template("welcome.html", name = input_name)
      else:
         return render_template("login.html", message = "Error: Wrong password")
   else:
      return render_template("login.html", message =  "Error: Wrong username")

@app.route("/profile")
def profile():
    #To be updated
    if "username" in session.keys():
        #flash(makeTable.getBlog(session['username']))
        return render_template("profile.html", name = session["username"])
    return redirect("/")

@app.route("/newblog")
def new_blog():
    form = cgi.FieldStorage()
    #content = form.getvalue('content')
    #print form
    #print request.args
    make.createBlog(session['username'],request.args['title'],request.args['content'])
    #createBlog(session['username'], form.getvalue('title'),form.getvalue('content'))
    return redirect(url_for("profile"))

@app.route("/feed")
def feed():
    #To be updated
    return render_template("feed.html")

@app.route("/logout")
def logged_out():
    session.pop("username") #Ends session
    return redirect("/") #Redirecting to login

if __name__ == "__main__":
    app.debug = True
    app.run()
