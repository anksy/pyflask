from database import db
from marshmallow import Schema, fields


class Category(db.Model):
    __tablename__ = "categories"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    description = db.Column(db.Text, default="", nullable=True)

    def __init__(self, title, description):
        self.title = title
        self.description = description

    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(id = id).first()

# register schema for category model
class CategorySchema(Schema):
    id = fields.Integer()
    title = fields.String(required=True)
