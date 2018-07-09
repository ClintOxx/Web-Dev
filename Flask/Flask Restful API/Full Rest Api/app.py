import os

from flask import Flask
from flask_jwt import JWT
from flask_restful import Api

from resources.item import Item, ItemList
from resources.store import Store, StoreList
from resources.user import UserRegister
from security import authenticate, identity

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']= os.environ.get('DATABASE_URL', 'sqlite:///data.db') #get db from env var or use the sqlite
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False  #flask sql alchemy will track every change, but actual SQLA has its own which we will use instead
app.secret_key = 'github' 
api = Api(app)


jwt = JWT(app, authenticate, identity) #/auth


#let api know the resource is accessible by api, passing the name to the class like @app.route
api.add_resource(Store, '/store/<string:name>')
api.add_resource(Item, '/item/<string:name>') 
api.add_resource(ItemList, '/items')
api.add_resource(StoreList, '/stores')
api.add_resource(UserRegister, '/register') #call UserRegister post method


if __name__ == '__main__':
    from db import db
    db.init_app(app) # avoid circular imports
    app.run(debug=True)
