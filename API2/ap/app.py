from flask import Flask
from flask_jwt_extended import JWTManager


# local import
from config import Development

#def create_app():

app = Flask(__name__, instance_relative_config=True)
app.config.from_object(Development)
from ap.database import Database
db = Database()

db.init_app(app)

from routes import questions ,user
app.register_blueprint(user.bPrint, url_prefix="/")
app.register_blueprint(questions.che, url_prefix="/")


#    return app
