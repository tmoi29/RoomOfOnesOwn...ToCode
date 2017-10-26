global c
from flask import flash
import sqlite3, random   #enable control of an sqlite database
from time import gmtime, strftime

f="info.db"

db = sqlite3.connect(f) #open if f exists, otherwise create
c = db.cursor()    #facilitate db ops

def db_setup():
	global c
	c = sqlite3.connect("info.db").cursor()
#	c.execute("SET sql_notes = 0;")
	c.execute("CREATE TABLE IF NOT EXISTS accounts(username TEXT PRIMARY KEY, pass TEXT);")
	c.execute("CREATE TABLE IF NOT EXISTS blogs(id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT, title TEXT, body TEXT, timestamp TEXT);")
#	c.execute("SET sql_notes = 1;")

#db_setup()

#Accounts
#==========================================================
"""
command = "CREATE TABLE accounts(username TEXT PRIMARY KEY, pass TEXT)"
c.execute(command)    #run SQL statement
"""
#Create an account
def createAcc(user, passw):
        try:
	        c_dup = db.cursor()
	        command = "INSERT INTO accounts VALUES(%s, %s)" %(user,passw)
	        c_dup.execute(command)
        except:
                flash("Username is already taken")
#==========================================================

#TESTS
#createAcc('"pep"', '"yoyo"')

#Blogs
#add an id num and make it primary key - use rand num generator
#==========================================================

#Create a blog
def createBlog(user, title, body):
                time = strftime("%Y-%m-%d %H:%M:%S", gmtime())
		command = "INSERT INTO blogs VALUES(%s,%s,%s,%s)" %(user, title, body, time)
		print command
		c.execute(command)
                """
        except:
                print "yo"
		#flash("Runtime error")
		#createBlog(user, title, body, time)"""

createBlog('"ajdlfkj"', '"dakfhksa"', '"hakdfjklsdjf"')

def updateBlog(idnum, title, body):
	try:
                time = time.sfrftime("%Y-%m-%d %H:%M:%S")
		command = """UPDATE blogs 
		SET title = %s , body = %s, time = %s 
		WHERE id = %d""" %(title, body, time, idnum)
		c.execute(command)
	except:
		print "wrong id"

def getBlog(user):
    global c
    c.execute("SELECT * FROM blogs WHERE username=?", (user,))
    return c.fetchall()

#==========================================================

#TESTS
#createBlog("'lol'", "'lel'", '"dfjaksjd"', '"djfaksdjf"')

db.commit() #save changes

db.close()  #close database




