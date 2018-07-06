import sqlite3
from db import db

class UserModel(db.Model):
    __tablename__ = "users" #sets name of table

    id = db.Column(db.Integer, primary_key=True)  #sql Alch creates columns based on the variables
    username = db.Column(db.String(80)) 
    password = db.Column(db.String(80))
    
    def __init__(self, _id, username, password):
        self.id = _id
        self.username = username
        self.password = password 

    @classmethod
    def find_by_username(cls, username):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query= "SELECT * FROM users WHERE username=?"
        result = cursor.execute(query, (username,)) #search users table to get back all results that match the username  
        row = result.fetchone()
        if row:    #using cls instead of self so it works with any class
            user = cls(*row) #getting info from the 3 columns, id, username and password and creating an User object. Use positional arg to accept all args
        else:
            user = None
        
        connection.close()
        return user


    @classmethod
    def find_by_id(cls, _id):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query= "SELECT * FROM users WHERE id=?"
        result = cursor.execute(query, (_id,)) 
        row = result.fetchone()
        if row:    
            user = cls(*row) 
        else:
            user = None
        
        connection.close()
        return user