
from flask import Blueprint
from flask_restx import Api
import os, importlib
from app.constants.swagger import config

# instantiating a blueprint of app
api_bp = Blueprint('api', __name__)

# creating api instance with swagger config
api = Api(api_bp, **config)

# module path
MODULES_PATH = "app/business"


def get_module_name(module):
    return remove_extension(module).title()


def get_module_import_file(filename):
    return remove_extension(filename.replace("/", "."))


def remove_extension(module):
    return module.replace(".py","")


# reading modules directory
for module in os.listdir(path=MODULES_PATH):
    # omitting unwanted modules
    if module not in {'response.py', '__pycache__'}:
        # loading all modules and registering into flask
        for controller in os.listdir("{path}/{module}".format(module=module, path=MODULES_PATH)):
            # omitting cache / remove
            if controller not in {'__pycache__', 'serializers.py'}:

                # getting route details
                module_path, controller_name = get_module_import_file(MODULES_PATH + "/" + module + "/" + controller), get_module_name(controller)

                # importing logical modules to be served when a route called
                _M = importlib.import_module(module_path)
                
                # adding route to flask 
                # module_class = getattr(_M, controller_name)
                
                if _M.ns:
                    # if module has namespace then register to api
                    api.add_namespace(_M.ns)
                    # api.add_resource(module_class, *module_class.__endpoints__)
                