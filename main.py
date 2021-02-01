from flask import Flask

app = Flask(__name__)                                                               # create instance of flask web application

from database import init_db                                                        # retrieve db setup from database file
db = init_db(app)                                                                   # inititalize database with app configuration

from flask_marshmallow import Marshmallow                                           # import marshmallow ()
ma = Marshmallow(app)                                                               # initialize instance of marshmallow

from controllers import registerable_controllers
for controller in registerable_controllers:
    app.register_blueprint(controller)                                              # register blueprint in app

from flask_bootstrap import Bootstrap
app.config.from_mapping(SECRET_KEY=b'\xd6\x04\xbdj\xfe\xed$c\x1e@\xad\x0f\x13,@G')
Bootstrap(app)