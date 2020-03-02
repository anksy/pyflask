from flask_restx import fields
from app import api

category_lists = {
    "category_id": fields.Integer(attribute="id"),
    "title": fields.String
}

ip_category_req = api.model('Category', {
    "name": fields.String
})