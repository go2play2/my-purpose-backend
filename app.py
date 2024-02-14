# app.py
from flask import Flask, jsonify, request, current_app
import json
from util import db_util


def create_app(test_config = None):
    app = Flask(__name__)

    if test_config is None:
        app.config.from_pyfile("config.py")
    else:
        app.config.update(test_config)


    @app.route("/ping", methods=['GET'])
    def ping():
        return "pong"


    @app.route("/sign-up", methods=['POST'])
    def sign_up():
        new_user = request.json
        print("### sign-up ###\n", new_user)
        new_user_id = insert_user(new_user)
        user = select_user(new_user_id)

        return jsonify(user)


    @app.route("/tweet", methods=['POST'])
    def tweet():
        user_tweet = request.json
        print("### tweet ###\n", user_tweet)
        user_id = int(user_tweet['id'])
        tweet = user_tweet['tweet']

        if len(tweet) > 300:
            return "최대 글자수(300자)를 초과했습니다.", 400
        
        insert_tweet(user_tweet)

        return '', 200



    @app.route("/follow", methods=['POST'])
    def follow():
        payload = request.json
        print("### follow ###\n", payload)

        user_id = int(payload['id'])
        user_id_to_follow = int(payload['follow'])

        if user_id not in app.users:
            return "사용자가 존재하지 않습니다.", 400

        if user_id_to_follow not in app.users:
            return "Follow 대상 사용자가 존재하지 않습니다.", 400

        user = app.users[user_id]
        user.setdefault('follow', set()).add(user_id_to_follow)
        print("=== user: ", user)

        return json.dumps(user, default=custom_json_set)



    @app.route("/unfollow", methods=['POST'])
    def unfollow():
        payload = request.json
        print("### unfollow ###\n", payload)

        user_id = int(payload['id'])
        user_id_to_unfollow = int(payload['unfollow'])

        if user_id not in app.users:
            return "사용자가 존재하지 않습니다.", 400

        if user_id_to_unfollow not in app.users:
            return "Unfollow 대상 사용자가 존재하지 않습니다.", 400

        user = app.users[user_id]
        user.setdefault('follow', set()).discard(user_id_to_unfollow)
        print("=== user: ", user)

        return json.dumps(user, default=custom_json_set)



    @app.route("/timeline/<int:user_id>", methods=['GET'])
    def timeline(user_id):
        print("### timeline ###\n")

        if user_id not in app.users:
            return "사용자가 존재하지 않습니다.", 400

        user = app.users[user_id]
        follow_list = user.get('follow', set())
        follow_list.add(user_id)


        timeline = [tweet for tweet in app.tweets if tweet['user_id'] in follow_list]

        print("=== timeline: ", timeline)

        result = {'user_id': user_id,
                'timeline': timeline}

        return json.dumps(result, default=custom_json_set)


    return app


# Private Methods
# -------------------------------------------------

def insert_user(user):
    con, cursor = db_util.get_connection()

    cursor.execute("""
        INSERT INTO mt_users (
            name,
            email,
            profile,
            hashed_password
        ) VALUES (%s, %s, %s, %s)
    """, (
        db_util.attr_value(user, 'name'), 
        db_util.attr_value(user, 'email'), 
        db_util.attr_value(user, 'profile'), 
        db_util.attr_value(user, 'password') )
    )

    new_user_id = cursor.lastrowid

    con.commit()
    db_util.close(con, cursor)

    print("*** new user inserted(id): ", new_user_id)
    return new_user_id


def select_user(user_id):
    con, cursor = db_util.get_connection()

    exe_result = cursor.execute("""
        SELECT 
            id,
            name,
            email,
            profile
        FROM mt_users
        WHERE id = %s
        """, (user_id,))
    
    print("=== execute result: ", exe_result)
    user = cursor.fetchone()

    print("=== user from DB: ", user)

    db_util.close(con, cursor)

    return user



def insert_tweet(user_tweet):
    con, cursor = db_util.get_connection()

    cursor.execute("""
        INSERT INTO mt_tweets (
            user_id,
            tweet
        ) VALUES ( %s, %s )
    """, (
        db_util.attr_value(user_tweet, 'id'), 
        db_util.attr_value(user_tweet, 'tweet'), 
    ))

    result = cursor.rowcount

    con.commit()
    db_util.close(con, cursor)

    print("*** new tweet inserted")
    return result



def custom_json_set(obj):
    if isinstance(obj, set):
        return list(obj)
    return obj


# app = Flask(__name__)

# app.users = {}
# app.tweets = []
# app.id_count = 1


