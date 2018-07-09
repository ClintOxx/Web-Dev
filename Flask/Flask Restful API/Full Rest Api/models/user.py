import sqlite3
from db import db

class UserModel(db.Model):
    __tablename__ = "users" #sets name of table

    id = db.Column(db.Integer, primary_key=True)  #sql Alch creates columns based on the variables
    username = db.Column(db.String(80)) 
    password = db.Column(db.String(80))
    
    def __init__(self, username, password):
        self.username = username
        self.password = password 

    def save_to_db(self): # passes in the username, password data after its built in  userregistration
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_by_username(cls, username):
        return cls.query.filter_by(username=username).first() # the first username is the table name not the argument


    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()