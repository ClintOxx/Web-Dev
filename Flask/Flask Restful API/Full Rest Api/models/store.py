from db import db


class StoreModel(db.Model):
    __tablename__='stores'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))

    items = db.relationship('ItemModel', lazy ='dynamic') #backref lets the store look up which items in the items table which has a store_id thats equal to its own store_id
    #one to many, there is no foreign key. This gives back a list


    def __init__(self, name):
        self.name = name


    
    def json(self):
        return {'name': self.name, 'items': [item.json() for item in self.items.all()]} #return json version of the item model. looks through the list "items" 

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()  # SELECT * FROM items WHERE name=name LIMIT 1



    def save_to_db(self):
        db.session.add(self)
        db.session.commit()



    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()


