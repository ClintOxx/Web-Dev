from flask import Flask, render_template

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
    pass


# GET/store/<string:name>
@app.route('/store/<string:name>', methods=['GET'])
def get_store(name):
    pass


#GET /store 
@app.route('/store')
def get_stores():
    pass

# POST /store/<string:name>/item 
@app.route('/store/<string:name>/item' , methods=['POST'])
def create_item_in_store(name):
    pass


# GET /store/<string:name>/item 
@app.route('/store/<string:name>/item')
def get_item_in_store(name):
    pass










app.run(port=5000)