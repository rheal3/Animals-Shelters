from flask_sqlalchemy import SQLAlchemy

def init_db(app):
    app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql+psycopg2://rebekahheal@localhost:5432/basics"       # set db_uri in app config
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False                                                    # set tracking mods to false in app config (don't need to shut down and rerun flask for changes to appear in the flask app)
    db = SQLAlchemy(app)                                                                                    # set db to instance of sqlalchemy & pass in instance of app
    return db