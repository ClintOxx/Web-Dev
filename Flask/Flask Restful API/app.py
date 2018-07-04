from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template



#POST /store data: {name:}

# GET/store/<string:name>

#GET /store 

# POST /store/<string:name>/item 

# GET /store/<string:name>/item 










app.run(port=5000)