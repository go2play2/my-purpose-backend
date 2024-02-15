import jwt
import bcrypt
import datetime

from model import UserDao
from util import str_util


class UserService:
    def __init__(self, config) -> None:
        self.user_dao = UserDao()
        self.config = config



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



    def follow(self, user_follow):
        self.user_dao.insert_follow(user_follow)


    def unfollow(self, user_unfollow):
        self.user_dao.delete_follow(user_unfollow)
