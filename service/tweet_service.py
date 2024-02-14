from model import TweetDao
from util import db_util


class TweetService:
    def __init__(self) -> None:
        self.tweet_dao = TweetDao()

    
    def tweet(self, user_tweet):
        return self.tweet_dao.insert_tweet(db_util.attr_value(user_tweet, 'id'), 
            db_util.attr_value(user_tweet, 'tweet'))
    
    
    def timeline(self, user_id):
        print("## timeline:", self, user_id)
        print("## timeline:", self.tweet_dao)
        timeline = self.tweet_dao.select_timeline(user_id)

        return {'user_id': user_id,
                'timeline': timeline}
