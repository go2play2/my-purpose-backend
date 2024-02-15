# app.py
from flask import Flask
from flask_cors import CORS
from control import common_control, user_control, tweet_control



def create_app(test_config = None):
    print("### Creating APP ###")
    app = Flask(__name__)

    if test_config is None:
        app.config.from_pyfile("config.py")
    else:
        app.config.update(test_config)

    CORS(app)

    common_control.create_endpoints(app)
    user_control.create_endpoints(app)
    tweet_control.create_endpoints(app)

    return app
