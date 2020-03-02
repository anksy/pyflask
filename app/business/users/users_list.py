from flask_restx import Resource
from app.business.response import Resposne
from app import api

users = [
    {
        "id": 1,
        "name": "Bhupendra"
    },
    {
        "id": 2,
        "name": "Singh"
    }
]

ns = api.namespace("users", description="Manage all Users")

@ns.route("")
class Users_List(Resource, Resposne):

    def get(self, **data):
        return self.success(data={"name": data.get("name")}) if data.get('name') else self.success(data=users)
    
    def post(self):
        return { "name" : "tester"}