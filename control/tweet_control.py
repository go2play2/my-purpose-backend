from flask import g, request
import json

from control.common_control import login_required
from service import TweetService
from util import str_util



def create_endpoints(app):

    tweet_service = TweetService()

    @app.route("/tweet", methods=['POST'])
    @login_required
    def tweet():
        user_tweet = request.json
        print("### tweet ###\n", user_tweet)
        tweet = user_tweet['tweet']
        
        print("*** Global variable(user_id):" , g.user_id)

        if len(tweet) > 300:
            return "최대 글자수(300자)를 초과했습니다.", 400
        
        tweet_service.tweet(user_tweet)

        return '', 200



    @app.route("/timeline/<int:user_id>", methods=['GET'])
    def timeline(user_id):
        print("### timeline ###\n")

        timeline = tweet_service.timeline(user_id)

        return json.dumps(timeline, default=str_util.custom_json_set)
