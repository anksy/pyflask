from database.Category import Category, CategorySchema
from database import db

# category schema
categories_schema = CategorySchema(many=True)
category_schema = CategorySchema()

class Category_DAO:
    # will return all the categories based
    # on filters
    @staticmethod
    def get_all_categories():
        category = Category.query.all()
        return categories_schema.dump(category).data

    # will add a new cateogry
    @staticmethod
    def add_new_category(category_obj):
        category = Category(**category_obj)
        db.session.add(category)
        # commit the changes
        db.session.commit()

        return category_schema.dump(category).data
