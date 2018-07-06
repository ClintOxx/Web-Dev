from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from security import authenticate, identity


from item import Item, ItemList
from user import UserRegister

app = Flask(__name__)
app.secret_key = 'github' 
api = Api(app)

jwt = JWT(app, authenticate, identity) #/auth


#let api know the Item resource is accessible by api, passing the name to the Item class like @app.route
api.add_resource(Item, '/item/<string:name>') 
api.add_resource(ItemList, '/items')
api.add_resource(UserRegister, '/register') #call UserRegister post method


if __name__ == '__main__':
    app.run(debug=True)







