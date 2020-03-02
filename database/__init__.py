from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

# instance of DB
db = SQLAlchemy()

# for schema vaildation
ma = Marshmallow()
