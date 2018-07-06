import sqlite3
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required



items = []

class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('price', type=float, required=True, help='This field cant be blank')

    @jwt_required()
    def get(self, name):
        item = self.find_by_name(name)
        if item:
            return item
        return{'message': 'item not found'}, 404


    @classmethod
    def find_by_name(cls, name):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor() 
        
        query = "SELECT * FROM items WHERE name=?"
        result= cursor.execute(query, (name,))
        row = result.fetchone()
        connection.close()
         
        if row:
            return {"item": {'name': row[0], 'price': row[1]}}   


    def post(self, name):
        if self.find_by_name(name):
            return {"message": f"item with name {name} already exists"}, 400
        
        data = Item.parser.parse_args()
        
        item = {'name' : name, 'price': data['price']}

        try:
            self.insert(item)
        except:
            return {'Message': "an error occured inserting the item"}, 500
        
        return item, 201


    @classmethod
    def insert(cls, item):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "INSERT INTO items VALUES(?, ?)"#.format(table=cls.TABLE_NAME)
        cursor.execute(query, (item['name'], item['price']))

        connection.commit()
        connection.close()


    def delete(self, name):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "DELETE FROM items WHERE name=?"
        cursor.execute(query, (name,))

        connection.commit()
        connection.close()
        return {'message': 'Item deleted'}

    
    
    #@jwt_required()
    def put(self, name):
        data = Item.parser.parse_args()
        item = self.find_by_name(name)

        updated_item = {'name': name, 'price': data['price']}
        if item is None:
            try:
                self.insert(updated_item)
            except:
                return {"message": "An error occurred inserting the item."}
        else:
            try:
                self.update(updated_item)
            except:
                raise
                return {"message": "An error occurred updating the item."}
        return updated_item



    @classmethod
    def update(cls, item):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "UPDATE items SET price=? WHERE name=?"#.format(table=cls.TABLE_NAME)
        cursor.execute(query, (item['price'], item['name']))

        connection.commit()
        connection.close()




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