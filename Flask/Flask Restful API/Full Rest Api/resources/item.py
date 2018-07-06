import sqlite3
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.item import ItemModel


class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('price', type=float, required=True, help='This field cant be blank')

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
        
        item = ItemModel(name, data['price'])   #passing variables instead of dict

        try:
            item.insert()
        except:
            return {'Message': "an error occured inserting the item"}, 500
        
        return item.json(), 201


    def delete(self, name):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "DELETE FROM items WHERE name=?"
        cursor.execute(query, (name,))

        connection.commit()
        connection.close()
        return {'message': 'Item deleted'}

    
    
    def put(self, name):
        data = Item.parser.parse_args()
        item = ItemModel.find_by_name(name)

        updated_item = ItemModel(name, data['price'])
        if item is None:
            try:
                updated_item.insert()
            except:
                return {"message": "An error occurred inserting the item."}
        else:
            try:
                updated_item.update() #using the new item info to update instead of using what ever old info "item" had
            except:
                raise
                return {"message": "An error occurred updating the item."}
        return updated_item.json()





class ItemList(Resource):
    TABLE_NAME = 'items'

    def get(self):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "SELECT * FROM {table}".format(table=self.TABLE_NAME)
        result = cursor.execute(query)
        items = []
        for row in result:
            items.append({'name': row[0], 'price': row[1]}) #getting all the items in a list by iterating through the data base and returning item list
        connection.close()

        return {'items': items}