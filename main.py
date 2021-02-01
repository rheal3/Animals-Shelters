from dotenv import load_dotenv
load_dotenv()

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow                                           # import marshmallow ()

db = SQLAlchemy()
ma = Marshmallow()                                                               # initialize instance of marshmallow

def create_app():
    app = Flask(__name__)                                                           # create instance of flask web application
    app.config.from_object("settings.app_config")

    db.init_app(app)
    ma.init_app(app)
# from database import init_db                                                        # retrieve db setup from database file
# db = init_db(app)                                                                   # inititalize database with app configuration


    from controllers import registerable_controllers
    for controller in registerable_controllers:
        app.register_blueprint(controller)                                              # register blueprint in app
    
    return app