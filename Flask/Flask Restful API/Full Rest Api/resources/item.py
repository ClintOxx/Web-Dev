from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.item import ItemModel


class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('price', type=float, required=True, help='This field cant be blank')

    parser.add_argument('store_id', type=int, required=True, help='Every item needs a store id')

    @jwt_required()
    def get(self, name):
        item = ItemModel.find_by_name(name)
        if item:
            return item.json() #convert the item object to json since db doesnt return json but an object
        return{'message': 'item not found'}, 404


    def post(self, name):
        if ItemModel.find_by_name(name):
            return {"message": f"item with name {name} already exists"}, 400
        
        data = Item.parser.parse_args()
        
        item = ItemModel(name, **data)   #passing variables instead of dict

        try:
            item.save_to_db()
        except:
            return {'Message': "an error occured inserting the item"}, 500
        
        return item.json(), 201


    def delete(self, name):
        item = ItemModel.find_by_name(name)
        if item:
            item.delete_from_db()
        return {'message': 'item deleted'}
    
    def put(self, name):
        data = Item.parser.parse_args()
        item = ItemModel.find_by_name(name)

        
        if item is None:
            item = ItemModel(name, data['price'], data['store_id'])
        else:
            item.price = data['price']
        item.save_to_db()
        
        return item.json()





class ItemList(Resource):
    def get(self):
        return {'items': [item.json() for item in ItemModel.query.all()]} # make a list of the items using list comp, convert each item into json