from flask import Flask, request
from flask_restful import Resource, Api


app = Flask(__name__)
api = Api(app)

items = []

class Item(Resource):
    def get(self, name):
        item = next(filter(lambda x: x['name'] == name, items), None) #going to loop through list, "items" is passed into x arg
        return {'item': item}, 200 if item else 404
    
    def post(self, name):
        if next(filter(lambda x: x['name'] == name, items), None):
            return {"message": f"item with name {name} already exists"}, 400
        
        data = request.get_json()
        item = {'name' : name, 'price': data['price']}
        items.append(item)
        return item, 201


class ItemList(Resource):
    def get(self):
        return {'items': items}


#let api know the Item resource is accessible by api, passing the name to the Item class like @app.route
api.add_resource(Item, '/item/<string:name>') 
api.add_resource(ItemList, '/items')


app.run(debug=True)







