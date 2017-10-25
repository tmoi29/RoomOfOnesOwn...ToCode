
import sqlite3, random   #enable control of an sqlite database

f="info.db"

db = sqlite3.connect(f) #open if f exists, otherwise create
c = db.cursor()    #facilitate db ops

#Accounts
#==========================================================
"""
command = "CREATE TABLE accounts(username TEXT PRIMARY KEY, pass TEXT)"
c.execute(command)    #run SQL statement
"""
#Create an account
def createAcc(user, passw):
    c_dup = db.cursor()
    command = "INSERT INTO accounts VALUES(%s, %s)" %(user,passw)
    c_dup.execute(command)
#==========================================================

#TESTS
#createAcc('"pep"', '"yoyo"')

#Blogs
#add an id num and make it primary key - use rand num generator
#==========================================================
"""
command = "CREATE TABLE blogs(id INTEGER PRIMARY KEY, username TEXT, title TEXT, body TEXT, timestamp TEXT)"
c.execute(command)    #run SQL statement
"""
    
#Create a blog
def createBlog(user, title, body, time):
    idnum = random.randint(1, 1000)
    try:
        command = "INSERT INTO blogs VALUES(%d,%s,%s,%s,%s)" %(idnum, user, title, body, time)
        print command
        c.execute(command)
    except:
        createBlog(user, title, body, time)

def updateBlog(idnum, title, body, time):
    try:
        command = """UPDATE blogs 
        SET title = %s , body = %s, time = %s 
        WHERE id = %d""" %(title, body, time, idnum)
        c.execute(command)
    except:
        print "wrong id"
#==========================================================

#TESTS
#createBlog("'lol'", "'lel'", '"dfjaksjd"', '"djfaksdjf"')

db.commit() #save changes

db.close()  #close database




