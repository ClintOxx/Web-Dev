import sqlite3



class ItemModel:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    
    def json(self):
        return {'name': self.name, 'price': self.price} #return json version of the item model

    @classmethod
    def find_by_name(cls, name):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor() 
        
        query = "SELECT * FROM items WHERE name=?"
        result= cursor.execute(query, (name,))
        row = result.fetchone()
        connection.close()
         
        if row:
            return cls(*row) # calling the ItemModel class itself to pass in the name and price properties (row[0], row[1])
            #into the result.fetchone function instead of typing them out



    def insert(self):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "INSERT INTO items VALUES(?, ?)"#.format(table=cls.TABLE_NAME)
        cursor.execute(query, (self.name, self.price))

        connection.commit()
        connection.close()



    def update(self):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "UPDATE items SET price=? WHERE name=?"#.format(table=cls.TABLE_NAME)
        cursor.execute(query, (self.price, self.name))

        connection.commit()
        connection.close()






