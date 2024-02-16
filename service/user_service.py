import os
import jwt
import bcrypt
import datetime
from werkzeug.utils import secure_filename
import boto3

from model import UserDao
from util import str_util


class UserService:
    def __init__(self, config) -> None:
        self.user_dao = UserDao()
        self.config = config
        self.s3 = boto3.client(
            "s3",
            aws_access_key_id = config['S3_ACCESS_KEY_ID'],
            aws_secret_access_key = config['S3_SECRET_KEY'],
        )



    def sign_up(self, new_user):
        new_user['password'] = bcrypt.hashpw(new_user['password'].encode('utf-8'), bcrypt.gensalt())
        new_user['profile'] = str_util.get_value(new_user, 'profile')
        new_user_id = self.user_dao.insert_user(new_user)
        user = self.user_dao.select_user_by_id(new_user_id)

        return user



    def login(self, email_pwd):
        email = email_pwd['email']
        password = email_pwd['password']
        
        user = self.user_dao.select_user_by_email(email)
        print("**", user)
        if not user or not user.get('hashed_password'):
            print("User not exist.")
            return None

        check_result = bcrypt.checkpw(password.encode('utf-8'), user['hashed_password'].encode('utf-8'))
        print("password check:", check_result)
        if not check_result:
            print('Password is not matched.')
            return None

        user_id = user['id']
        
        payload = {
            'user_id': user_id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes = 60 * 24)
        }

        token = jwt.encode(payload, self.config['JWT_SECRET_KEY'], 'HS256')
        print("* new jwt token created *\n", token)
        jwtToken = {
                'access_token': token
            }
        return jwtToken



    def save_profile_picture(self, user_id, profile_pic):
        filename = secure_filename(profile_pic.filename)
        
        print("** secured file name:", filename)
        
        # 로컬 디스크 저장
        # file_path = os.path.join('./profile_pictures', filename);
        # profile_pic.save(file_path)
        
        # S3 저장
        self.s3.upload_fileobj(
            profile_pic,
            self.config['S3_BUCKET_NAME'],
            filename
        )
        # https://my-purpose-bucket.s3.ap-northeast-2.amazonaws.com/1692999734638.jpg
        file_path = f"{self.config['S3_BUCKET_URL']}/{filename}"

        self.user_dao.udpate_profile_picture(user_id, file_path)



    def get_profile_picture(self, user_id):
        result = self.user_dao.select_profile_picture(user_id)
        
        print("Profile picture:", result)
        return result['profile_picture'] if result else ''



    def follow(self, user_follow):
        self.user_dao.insert_follow(user_follow)


    def unfollow(self, user_unfollow):
        self.user_dao.delete_follow(user_unfollow)
