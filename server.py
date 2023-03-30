from flask import Flask, request
from flask_restful import Resource, Api
import json

app = Flask(__name__)
api = Api(app)

class Users(Resource):
    def get(self):
        data = readFromFile()
        return data

    def post(self):
        name = request.json['name']
        email = request.json['email']
        data = readFromFile()
        id = data[-1]["id"] + 1 if len(data) > 0 else 0
        data.append({
            "id": id,
            "name": name,
            "email": email
        })
        writeInFile(data)
        return data

class User(Resource):
    def get(self, id):
        data = readFromFile()
        return findItem(data, id)

    def delete(self, id):
        data = readFromFile()
        item = findItem(data,id)
        data.remove(item)
        writeInFile(data)
        return {"status": "success"}

    def put(self, id):
        name = request.json['name']
        email = request.json['email']
        data = readFromFile()
        item = findItem(data,id)
        item["name"] = name
        item["email"] = email
        writeInFile(data)
        return data
        
def findItem(data, id):
    for x in data:
        if x["id"] == int(id):
            return x
    else:
        return []

def readFromFile():
    with open('db.json', 'r') as openfile:
        return json.load(openfile)

def writeInFile(data):
    with open('db.json', 'w') as openfile:
        json.dump(data, openfile)

api.add_resource(Users, '/users')
api.add_resource(User, '/users/<id>')

if __name__ == '__main__':
    app.run(host="localhost", port=8001, debug=True)