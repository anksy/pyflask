from flask import Flask
from dotenv import load_dotenv

# loading env file
load_dotenv(".env")

# initial flask app instance
class Serve:
    def __init__(self, config):
        self.app = Flask(__name__)
        self.app.config.from_object(config)

    def register_blueprint_with_db(self):
        from app import api_bp

        @self.app.route("/")
        def index():
            return "/"
            
        self.app.register_blueprint(api_bp, url_prefix="/api/v1")

        from database import db
        db.init_app(self.app)

    def get_instance(self):
        # register app blueprint
        self.register_blueprint_with_db()

        # return app instance
        return self.app


if __name__ == '__main__':
    Serve("config").get_instance().run(debug=True)
