from flask import Flask, request
import json


def create_endpoints(app, services):
    user_service = services.user_service
    tweet_service = services.tweet_service
    
    
    @app.route("/ping", methods=['GET'])
    def ping():
        return "pong"


    @app.route("/sign-up", methods=['POST'])
    def sign_up():
        new_user = request.json
        print("### sign-up ###\n", new_user)
        user = user_service.sign_up(new_user)

        return json.dumps(user, default=custom_json_set)



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



    @app.route("/tweet", methods=['POST'])
    def tweet():
        user_tweet = request.json
        print("### tweet ###\n", user_tweet)
        tweet = user_tweet['tweet']

        if len(tweet) > 300:
            return "최대 글자수(300자)를 초과했습니다.", 400
        
        tweet_service.tweet(user_tweet)

        return '', 200



    @app.route("/timeline/<int:user_id>", methods=['GET'])
    def timeline(user_id):
        print("### timeline ###\n")

        timeline = tweet_service.timeline(user_id)

        return json.dumps(timeline, default=custom_json_set)


# Private Methods
# -------------------------------------------------

def custom_json_set(obj):
    if isinstance(obj, set):
        return list(obj)
    return obj
