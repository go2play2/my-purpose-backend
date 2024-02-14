from model import UserDao
from util import db_util


class UserService:
    def __init__(self) -> None:
        self.user_dao = UserDao()

    
    def sign_up(self, new_user):
        new_user_id = self.user_dao.insert_user(new_user)
        user = self.user_dao.select_user(new_user_id)

        return user


    def follow(self, user_follow):
        self.user_dao.insert_follow(user_follow)


    def unfollow(self, user_unfollow):
        self.user_dao.delete_follow(user_unfollow)

