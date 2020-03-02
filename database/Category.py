from database import db, ma
from marshmallow import Schema, fields


class Category(db.Model):
    __tablename__ = "categories"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)

    def __init__(self, title):
        self.title = title


# register schema for category model
class CategorySchema(Schema):
    id = fields.Integer()
    title = fields.String(required=True)
