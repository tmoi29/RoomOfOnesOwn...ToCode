
import sqlite3   #enable control of an sqlite database

f="info.db"

db = sqlite3.connect(f) #open if f exists, otherwise create
c = db.cursor()    #facilitate db ops

#Accounts
#==========================================================
command = "CREATE TABLE accounts(username TEXT PRIMARY KEY, pass TEXT)"
c.execute(command)    #run SQL statement

#Create an account
def createAcc(user, passw):
    command = "INSERT INTO accounts VALUES(" + user + ", " + passw + ")"
    c.execute(command)
#==========================================================

#Blogs
#add an id num and make it primary key - use rand num generator
#==========================================================
command = "CREATE TABLE blogs(username TEXT, title TEXT, body TEXT, timestamp TEXT)"
c.execute(command)    #run SQL statement

#Create a blog
def createBlog(user, title, body, time):
    
    command = "INSERT INTO accounts VALUES(%s,%s,%s,%s)" %(user, title, body, time)
    c.execute(command)

def updateBlog(user, title, body, time):
    command = """UPDATE accounts VALUES(%s,%s,%s,%s)" %(user, title, body, time)
    c.execute(command)
#==========================================================


db.commit() #save changes

db.close()  #close database




