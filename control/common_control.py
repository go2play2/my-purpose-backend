from functools import wraps

from flask import Response, current_app, request, g
import jwt


def create_endpoints(app):

    @app.route("/ping", methods=['GET'])
    def ping():
        return "pong"



def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        access_token = request.headers.get('Authorization')
        print("### Authorization Check ###\n", access_token)
        if access_token is None:
            print("[Error] Token is none !")
            return Response(status=401)

        try:
            sec_key = current_app.config['JWT_SECRET_KEY']
            algo = 'HS256'
            payload = jwt.decode(access_token, sec_key, algo)
        except jwt.InvalidTokenError:
            print("[Error] !!! Invalid Token !!!")
            payload = None
        
        if payload is None:
            return Response(status=401)
        
        user_id = payload['user_id']
        g.user_id = user_id

        return f(*args, **kwargs)
    return decorated_function
    