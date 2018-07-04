from flask import Flask, jsonify, request,  render_template

app = Flask(__name__)

stores = [
    {
        'name': 'My Store',
        'items': [{'name':'my item', 'price': 15.99 }]
    }
]


""" @app.route('/')
def home():
    return render_template """



#POST /store data: {name:}
@app.route('/store', methods =['POST'])
def create_store():
    request_data = request.get_json() #converts json string to dictionary
    new_store = {
        'name': request_data['name'], #getting the value from the {name:} key that was sent to us
        'items': []
    }
    stores.append(new_store) #addes the store we created to the stores list
    return jsonify(new_store) #returning the store to browser in json to confirm we made it.


# GET/store/<string:name>
@app.route('/store/<string:name>', methods=['GET'])
def get_store(name):
    for store in stores: # saves dictionary variable "store" from the list stores
        if store['name'] == name: #the value of the arg(name) passed in matches the value of the "{name:}"" dictionary key in "store" 
            return jsonify(store) #dont have to convert since its not a list but a dictionary(store)
    return jsonify({'message': 'store not found'})


#GET /store 
@app.route('/store')
def get_stores():
    return jsonify({'stores':stores}) #made the list "stores" into a dictionary called stores, so jsonify can convert it to json


# POST /store/<string:name>/item 
@app.route('/store/<string:name>/item' , methods=['POST'])
def create_item_in_store(name):
    request_data = request.get_json() 
    for store in stores:
        if store['name'] == name:
            new_item = {
                'name': request_data['name'], #getting the value from the {name:} key that was sent to us
                'price':request_data['price']
            }
            store['items'].append(new_item) #adds the new_item dictionary to the items list in the store dictionary
            return jsonify(new_item)  
    return jsonify({'message': 'store not found'})

# GET /store/<string:name>/item 
@app.route('/store/<string:name>/item')
def get_item_in_store(name):
    for store in stores:
        if store['name'] == name: #see if the key dictionary values match
            return jsonify({'items': store['items']}) # the key ["items"] has a value that is a list. its in the "store" dictionary, convert to dictionary 
    return jsonify({'message': 'item not found'})










app.run(port=5000, debug=True)