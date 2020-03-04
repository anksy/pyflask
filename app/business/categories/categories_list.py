from flask_restx import Resource, fields, marshal, reqparse
from app.business.response import Resposne
from app import api
from app.business.categories.serializers import category_lists, ip_category_req
from app.infra.category_dao import Category_DAO

# generating namespace for category controller
ns = api.namespace("categories", description="Manage all categories - REST endpoints")

@ns.route("")
class Categories_List(Resource, Resposne):

    @api.doc(responses={200: 'Success', 400: 'Bad Request'})
    def get(self):
        try:
            categories = Category_DAO.get_all_categories()
            result = marshal(categories, category_lists)
            return self.success(data=result)
        except TypeError as error:
            print(error)
        

    @api.expect(ip_category_req)
    def post(self):
        try:
            # extract data from request
            parser = reqparse.RequestParser()
            parser.add_argument('name', dest="title", required=True, type=str)
            args = parser.parse_args()

            # add new category
            category = Category_DAO.add_new_category(args)

            return self.success(data=category, msg="Category has been added")
        except:
            pass
        