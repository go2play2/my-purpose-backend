from flask import request
import json

from control.common_control import login_required
from service import UserService
from util import str_util



def create_endpoints(app):

    user_service = UserService(app.config)


    @app.route("/sign-up", methods=['POST'])
    def sign_up():
        new_user = request.json
        print("### sign-up ###\n", new_user)
        user = user_service.sign_up(new_user)

        return json.dumps(user, default=str_util.custom_json_set)



    @app.route("/login", methods=['POST'])
    def login():
        email_pwd = request.json
        print("### login ###\n", email_pwd)
        token = user_service.login(email_pwd)
        if token:
            return json.dumps(token, default=str_util.custom_json_set)
        else:
            return '', 401



    @app.route("/follow", methods=['POST'])
    @login_required
    def follow():
        user_follow = request.json
        print("### follow ###\n", user_follow)

        user_service.follow(user_follow)

        return '', 200



    @app.route("/unfollow", methods=['POST'])
    @login_required
    def unfollow():
        user_unfollow = request.json
        print("### unfollow ###\n", user_unfollow)

        user_service.unfollow(user_unfollow)

        return '', 200
