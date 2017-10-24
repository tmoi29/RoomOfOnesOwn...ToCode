
import sqlite3   #enable control of an sqlite database

f="info.db"

db = sqlite3.connect(f) #open if f exists, otherwise create
c = db.cursor()    #facilitate db ops

#Accounts
#==========================================================
command = "CREATE TABLE accounts(username TEXT PRIMARY KEY, pass TEXT)"
c.execute(command)    #run SQL statement
#==========================================================

#Blogs
#==========================================================
command = "CREATE TABLE blogs(username TEXT, title TEXT, body TEXT, timestamp TEXT)"
c.execute(command)    #run SQL statement
#==========================================================

db.commit() #save changes

db.close()  #close database


