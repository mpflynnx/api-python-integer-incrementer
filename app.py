from flask import Flask, jsonify, request
from flask_restful import Api, Resource

# Azure cosmod db sdk import needed

# Create a Flask object
app = Flask(__name__)

# Define as an Api our Flask object
api = Api(app)

# configure Azure cosmos db below
#
#

class Incrementer(Resource):
    def get(self):
        previous_number = db_number.find({})[0]["number"] # access index 0 of list
        new_number = previous_number + 1
        db_number.update_one({}, {"$set": {"number": new_num}})
        return new_number

api.add_resource(Incrementer, "/increment")

if __name__ == "__main__":
    app.run(host="0.0.0.0")
