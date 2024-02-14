# app.py
from flask import Flask
from service import UserService, TweetService
from control import create_endpoints


class Services:
    pass


def create_app(test_config = None):
    app = Flask(__name__)

    if test_config is None:
        app.config.from_pyfile("config.py")
    else:
        app.config.update(test_config)


    services = Services
    services.user_service = UserService()
    services.tweet_service = TweetService()

    create_endpoints(app, services)

    return app
