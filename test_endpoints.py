import json
import pytest
from app import create_app


@pytest.fixture
def api():
    app = create_app()
    app.config['TEST'] = True
    api = app.test_client()
    
    return api



def test_ping(api):
    resp = api.get('/ping')
    assert b'pong' == resp.data


def x_test_sign_up(api):
    ## 테스트 사용자 생성
    new_user = {
        'email': 'jaehoon5@jaehoon.com',
        'password': '1234',
        'name': 'jaehoon5',
        'profile': 'runner',
    }
    
    resp = api.post(
        '/sign-up',
        data = json.dumps(new_user),
        content_type = 'application/json'
    )

    assert resp.status_code == 200

    ## 사용자 정보 조회
    resp_json = json.loads(resp.data)
    new_user_id = resp_json['id']
    print(new_user_id)



def test_tweet(api):
    new_user_id = 44
    
    ## 로그인
    resp = api.post(
        '/login',
        data = json.dumps({
            'email': 'jaehoon5@jaehoon.com',
            'password': '1234'
        }),
        content_type = 'application/json'
    )
    resp_json = json.loads(resp.data)
    access_token = resp_json['access_token']
    
    ## tweet 생성
    resp = api.post(
        '/tweet',
        data = json.dumps({
            'id': new_user_id,
            'tweet': 'I am 44.'
        }),
        content_type = 'application/json',
        headers = {
            'Authorization': access_token
        }
    )
    assert resp.status_code == 200


    ## tweet 확인
    resp = api.get(f'/timeline/{new_user_id}')
    assert resp.status_code == 200

    tweets = resp.data.decode('utf-8')
    print("** Tweets:", tweets)
    assert len(tweets) > 10



def test_unauthorized(api):
    # access token이 없이는 401 응답을 리턴하는지를 확인
    resp = api.post(
        '/tweet', 
        data         = json.dumps({'tweet' : "Hello World!"}),
        content_type = 'application/json'
    )
    assert resp.status_code == 401

    resp  = api.post(
        '/follow',
        data         = json.dumps({'follow' : 2}),
        content_type = 'application/json'
    )
    assert resp.status_code == 401

    resp  = api.post(
        '/unfollow',
        data         = json.dumps({'unfollow' : 2}),
        content_type = 'application/json'
    )
    assert resp.status_code == 401
