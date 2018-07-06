import sqlite3
from flask_restful import Resource, reqparse


class User:
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


class UserRegister(Resource):
    TABLE_NAME = 'users'

    parser = reqparse.RequestParser()
    parser.add_argument('username',
                        type=str,
                        required=True,
                        help="This field cannot be left blank!"
                        )
    parser.add_argument('password',
                        type=str,
                        required=True,
                        help="This field cannot be left blank!"
                        )

    
    def post(self):
        
        data = UserRegister.parser.parse_args()

        if User.find_by_username(data['username']): #check to see if it returns true or none
            return {"message": "User with that username already exists."}, 400

        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "INSERT INTO {table} VALUES (NULL, ?, ?)".format(table=self.TABLE_NAME)
        cursor.execute(query, (data['username'], data['password']))

        connection.commit()
        connection.close()

        return {"message": "User created successfully."}, 201