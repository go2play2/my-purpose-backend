# app.py
from flask import Flask
from control import user_control, tweet_control



def create_app(test_config = None):
    app = Flask(__name__)

    if test_config is None:
        app.config.from_pyfile("config.py")
    else:
        app.config.update(test_config)

    user_control.create_endpoints(app)
    tweet_control.create_endpoints(app)

    return app
