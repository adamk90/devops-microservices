from flask import Flask
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)

staff = [
    {
        "name": "Zoltan",
        "age": 35,
        "occupation": "DevOps Engineer"
    },
    {
        "name": "Tamas",
        "age": 38,
        "occupation": "Java Developer"
    },
    {
        "name": "Marton",
        "age": 25,
        "occupation": "DevOps Intern"
    }
]

class Staff(Resource):
    def get(self, name):
        for member in staff:
            if(name == member["name"]):
                return member, 200
        return "Member not found", 404

    def post(self, name):
        parser = reqparse.RequestParser()
        parser.add_argument("age")
        parser.add_argument("occupation")
        args = parser.parse_args()

        for member in staff:
            if(name == member["name"]):
                return "Member with name {} already exists".format(name), 400

        member = {
            "name": name,
            "age": args["age"],
            "occupation": args["occupation"]
        }
        staff.append(member)
        return member, 201

    def put(self, name):
        parser = reqparse.RequestParser()
        parser.add_argument("age")
        parser.add_argument("occupation")
        args = parser.parse_args()

        for member in staff:
            if(name == member["name"]):
                member["age"] = args["age"]
                member["occupation"] = args["occupation"]
                return member, 200

        member = {
            "name": name,
            "age": args["age"],
            "occupation": args["occupation"]
        }
        staff.append(member)
        return member, 201

    def delete(self, name):
        global staff
        staff = [member for member in staff if member["name"] != name]
        return "{} is deleted.".format(name), 200

api.add_resource(Staff, "/staff/<string:name>")

app.run(port=8888,host='0.0.0.0')
