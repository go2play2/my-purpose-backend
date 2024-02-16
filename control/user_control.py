from flask import request, send_file
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


    # Profile picture 등록
    @app.route("/profile_picture/<int:user_id>", methods=['POST'])
    def update_profile_picture(user_id):
        print("### update_profile_picture ###\n", request.files)
        if 'profile_pic' not in request.files:
            print(" ~ profile_pic file is missing !!")
            return "File is missing.", 404
        
        profile_pic = request.files['profile_pic']
        
        if profile_pic.filename == '':
            print(" ~ profile_pic file name is missing !!")
            return 'File name is missing.', 404
        
        user_service.save_profile_picture(user_id, profile_pic)

        return '', 200


    # Profile picture 조회
    @app.route("/profile_picture/<int:user_id>", methods=['GET'])
    def get_profile_picture(user_id):
        print("### get_profile_picture ###")
        profile_pic = user_service.get_profile_picture(user_id)

        if profile_pic:
            # 로컬 파일 전송
            # return send_file(profile_pic)
            # aws 파일 정보 전송
            return json.dumps({'img_url': profile_pic}, default=str_util.custom_json_set)
        else:
            return '', 404



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
