from flask import request
import json

from service import UserService
from util import str_util



def create_endpoints(app):

    user_service = UserService()


    @app.route("/ping", methods=['GET'])
    def ping():
        return "pong"


    @app.route("/sign-up", methods=['POST'])
    def sign_up():
        new_user = request.json
        print("### sign-up ###\n", new_user)
        user = user_service.sign_up(new_user)

        return json.dumps(user, default=str_util.custom_json_set)



    @app.route("/follow", methods=['POST'])
    def follow():
        user_follow = request.json
        print("### follow ###\n", user_follow)

        user_service.follow(user_follow)

        return '', 200



    @app.route("/unfollow", methods=['POST'])
    def unfollow():
        user_unfollow = request.json
        print("### unfollow ###\n", user_unfollow)

        user_service.unfollow(user_unfollow)

        return '', 200
