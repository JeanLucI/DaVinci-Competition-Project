from flask import Flask

from flask_cors import CORS

from .extensions import mongo

from .main import main

def create_app(config_object='UserDB.settings'):
    
    app = Flask(__name__)

    app.config.from_object(config_object)

    mongo.init_app(app)

    CORS(app)

    app.register_blueprint(main)

    return app