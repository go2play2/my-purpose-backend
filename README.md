# Run flask (linux)
FLASK_APP=app.py FLASK_DEBUG=1 flask run --host 0.0.0.0

# Run flask (windows)
flask run --host 0.0.0.0 --debug


# Run test
pytest -p no:warnings -vv



### 기타 (AWS - ubuntu 설정) ###

# aws 접속

<!-- my-purpose #1 -->
ssh -i "d:\Hobby\Aws\jaehoon.pem" ubuntu@43.200.177.146

<!-- my-purpose #2 -->
ssh -i "d:\Hobby\Aws\jaehoon.pem" ubuntu@3.34.179.163


# miniconda 설치
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
sh Miniconda3-latest-Linux-x86_64.sh

# python 설정
sudo apt-get update
sudo apt-get install python3-pip python3-venv

git clone https://github.com/go2play2/my-purpose-backend.git

cd my-purpose-backend
python3 -m venv .venv
source .venv/bin/activate

# package 설치
(.venv) pip install -r requirements.txt
# or
(.venv) pip install flask Flask-Cors PyJWT bcrypt mysql-connector-python boto3 pytest

# 서버 부팅 후 flask 실행
source .venv/bin/activate
(.venv) pip install flask Flask-Cors PyJWT bcrypt mysql-connector-python boto3 pytest
nohup flask run --host 0.0.0.0 &

