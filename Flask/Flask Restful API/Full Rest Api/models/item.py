from db import db


class ItemModel(db.Model):
    __tablename__='items'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    price = db.Column(db.Float(precision=2))

    store_id = db.Column(db.Integer, db.ForeignKey('stores.id')) #gets the id from the id field in the stores table
    store = db.relationship('StoreModel') # item property that lets sql that each item is related to only one store. many to one
    # it sets a property that shows which store in the Store table the store_id is attached to
    

    def __init__(self, name, price, store_id):
        self.name = name
        self.price = price
        self.store_id = store_id

    
    def json(self):
        return {'name': self.name, 'price': self.price} #return json version of the item model

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()  # SELECT * FROM items WHERE name=name LIMIT 1



    def save_to_db(self):
        db.session.add(self)
        db.session.commit()



    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()






