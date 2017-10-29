#A ROOM OF ONE'S OWN...TO CODE
#Irene Lam, Tiffany Moi, Carol Pan
#SoftDev pd7
#P00 - Da Art of Storytellin' 

global db
#from flask import flash
import sqlite3, random   #enable control of an sqlite database
import hashlib
from time import gmtime, strftime

def open_db():
    global db
    f="blogging.db"
    db = sqlite3.connect(f, check_same_thread = False) #open if f exists, otherwise create
    #c = db.cursor()    #facilitate db ops
    return

def close():
    global db
    db.commit() #save changes
    db.close()  #close database
    return

def db_setup():
    global db
    open_db()
    c_dup = db.cursor()
    c_dup.execute("CREATE TABLE IF NOT EXISTS accounts(username TEXT PRIMARY KEY, pass TEXT)")
    c_dup.execute("CREATE TABLE IF NOT EXISTS blogs(id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, username TEXT, title TEXT, body TEXT, timestamp DEFAULT CURRENT_TIMESTAMP NOT NULL)")

    #the breakdown:
    '''
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL
        -fills in id with rowid (which increments) unless specific value is given
    timestamp DEFAULT CURRENT_TIMESTAMP NOT NULL
        -fills in timestamp with SQLite time unless specific value is given
    '''
    close()
    return


#Accounts
#==========================================================

#Create an account
#-----------------
def createAcc(user, passw):
    global db
    try:
        open_db()
        c_dup = db.cursor()
        hash_object = hashlib.sha224(passw)
        hashed_pass = hash_object.hexdigest()
        command = "INSERT INTO accounts VALUES(\"%s\", \"%s\")" %(user,hashed_pass)
        print command
        c_dup.execute(command)
        close()
    except:
        print "Error in Account Creation: Username already taken."
        return False
    return True
#==========================================================

#For authentication stuff
#returns list of [user_exists, passw]
def auth(user):
    response = []
    open_db()
    c_dup = db.cursor()
    command = "SELECT username FROM accounts WHERE username = %s" %(user)
    c_dup.execute(command)
    users = c_dup.fetchall()
    if len(users) == 0:
        response.append(False)
    else:
        response.append(True)
        command = "SELECT pass FROM accounts WHERE username = %s" %(user)
        c_dup.execute(command)
        pwds = c_dup.fetchall()
        for passw in pwds:
            response.append(passw)
            print passw
    close()
    return response
        

#Blogs
#utilize SQL's ROWID functionality for identification
#==========================================================
#Create a blog post
def createBlog(user, title, body):
    global db
    try:
        if title == "" or len(body) < 1 or body == "Enter text here...":
            raise NameError
        open_db()
        c_dup = db.cursor()
        command = "INSERT INTO blogs(username, title, body) VALUES(\"%s\",\"%s\",\"%s\")" %(user, title, body)
        print command
        c_dup.execute(command)
        close()
    except:
        print "ERROR CREATING BLOG POST"
        return False
    return True

#Update a blog post
def updateBlog(idnum, title, body):
    global db
    try:
        open_db()
        c_dup = db.cursor()
        timestamp = strftime("%Y-%m-%d %H:%M:%S")
        print timestamp       
        command = "UPDATE blogs SET title = \"%s\", body = \"%s\", timestamp = \"%s\" WHERE id = %d" %(title, body, timestamp, idnum)
        print command
        c_dup.execute(command)
        close()
    except:
        print "UPDATE ERROR: NO SUCH ID"
        return False    
    return True

#procure a blog post
def getBlog(user):
    global db
    open_db()
    c_dup = db.cursor()
    try:
        command = "SELECT * FROM blogs WHERE username=\"%s\"" %(user)
        #print command
        c_dup.execute(command)
        posts = c_dup.fetchall()
        close()
    except:
        print "Error: Called on uncallable user"
        posts = []
    return posts

def getBlogs():
    global db
    open_db()
    c_dup = db.cursor()
    try:
        #print command
        c_dup.execute("SELECT * FROM blogs ORDER BY id DESC")
        posts = c_dup.fetchall()
        close()
    except:
        print "Error: Something went wrong.. missing setup?"
        posts = []
    return posts
    

#==========================================================
#TESTS
#createAcc("jack", "jackpwd")
#createAcc("lils", "lilspwd")
#createBlog("lol", "lel", "dfjaksjd")
#updateBlog(2, "sry fell asleep", "won't happen again")
#print getBlog("lol")
#createBlog("emily", "testing", "does this still work?") #so it does
