from flask import Flask
from flask_jwt_extended import JWTManager
from database import Database
db = Database()

# local import
from instance.config import app_config

def create_app(config_name):

    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])

    db.init_app(app)

    from application import routes
    app.register_blueprint(routes.bPrint, url_prefix="/")

    return app
