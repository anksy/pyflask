import os
# setting an env
DEBUG = True

# setting base dir
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

# grouping/bundling errore
BUNDLE_ERRORS = True

# defining the databaes
SQLALCHEMY_DATABASE_URI = os.getenv("DB")
SQLALCHEMY_TRACK_MODIFICATIONS = False

# Swagegr config
SWAGGER_SUPPORTED_SUBMIT_METHODS = ["get", "post", "put", "delete", "patch"]
SWAGGER_UI_DOC_EXPANSION = "list"
RESTPLUS_MASK_SWAGGER = False
SWAGGER_UI_OPERATION_ID = False
SWAGGER_UI_REQUEST_DURATION = True
RESTX_VALIDATE = True  # validate input data into api
