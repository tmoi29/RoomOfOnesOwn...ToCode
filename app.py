from flask import Flask, render_template, request, session, redirect
import os

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
    if "username" in session.keys():
       return render_template("welcome.html", name = session["username"])
    return render_template("login.html", message = "")

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
    return render_template("profile.html")

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
