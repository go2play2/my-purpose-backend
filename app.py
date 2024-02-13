# app.py
from flask import Flask, jsonify, request
from json import JSONEncoder


class CustomJsonEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, set):
            return list(obj)
        
        return JSONEncoder.default(self, obj)


app = Flask(__name__)

app.json_encoder = CustomJsonEncoder

app.users = {}
app.tweets = []
app.id_count = 1


@app.route("/ping", methods=['GET'])
def ping():
    return "pong"


@app.route("/sign-up", methods=['POST'])
def sign_up():
    new_user = request.json
    print("### sign-up ###\n", new_user)
    new_user["id"] = app.id_count
    app.users[new_user["id"]] = new_user
    app.id_count += 1

    return jsonify(new_user)



@app.route("/tweet", methods=['POST'])
def tweet():
    payload = request.json
    print("### tweet ###\n", payload)
    user_id = int(payload['id'])
    tweet = payload['tweet']

    if user_id not in app.users:
        return "사용자가 존재하지 않습니다.", 400
    
    if len(tweet) > 300:
        return "최대 글자수(300자)를 초과했습니다.", 400
    
    app.tweets.append({
        'user_id': user_id,
        'tweet': tweet,
    })

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

    return jsonify(user)

