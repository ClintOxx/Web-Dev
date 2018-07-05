from flask import Flask, jsonify, request,  render_template

app = Flask(__name__)

from flask import Flask
from flask_restful import Resource, Api


app = Flask(__name__)
api = Api(app)


class Student(Resource):
    def get(self, name): # resource for the get method
        return{'student': name}


#let api know the Student resource is accesable by api, passing the name to the Student class like @app.route
api.add_resource(Student, '/student/<string:name>') # example http://127.0.0.1:5000/student/Rolf



app.run(debug=True)







