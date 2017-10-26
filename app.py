from flask import Flask, render_template, request, session, redirect, flash, url_for
from makeTable import createBlog, db_setup, getBlog
import os, cgi

app = Flask (__name__)

the_username = "user" #Hardcoded username
the_password = "pwd"  #Hardcoded password
app.secret_key = os.urandom(32)

@app.route("/")
def hello_world():
    '''
    If session has a record of the correct username and password input, the user is logged in
    Otherwise, the login page is displayed
    '''
    db_setup()
    if "username" in session.keys():
       return render_template("welcome.html", name = session["username"])
    return render_template("login.html", message = "")

@app.route("/createaccount")
def create_account():
    return render_template("createaccount.html")

@app.route("/auth")
def check_creation():
    #if request.args["username"] is unique will do later
    if request.args["password1"] == request.args["password2"]:
        #add in stuff
        flash("Success!")
        return redirect(url_for("hello_world"))
    else:
        flash("Passwords do not match :(")
        return redirect(url_for("create_account"))


@app.route("/welcome")
def logged_in():
   input_name = request.args["username"]
   input_pass = request.args["password"]

   #Validation process, what went wrong (if anything)?
   if input_name == the_username:
      if input_pass == the_password:
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
        flash(getBlog(session['username']))
        return render_template("profile.html", name = session["username"])
    return redirect("/")

@app.route("/newblog")
def new_blog():
    form = cgi.FieldStorage()
    #content = form.getvalue('content')
    #print form
    #print request.args
    createBlog(session['username'],request.args['title'],request.args['content'], 'CURRENT_TIMESTAMP')
    #createBlog(session['username'], form.getvalue('title'),form.getvalue('content'), 'CURRENT_TIMESTAMP')
    return redirect(url_for("profile"))

@app.route("/about")
def about():
    #To be updated
    return render_template("about.html")

@app.route("/logout")
def logged_out():
    session.pop("username") #Ends session
    return redirect("/") #Redirecting to login

if __name__ == "__main__":
    app.debug = True
    app.run()
