# Run flask (linux)
FLASK_APP=app.py FLASK_DEBUG=1 flask run --host 0.0.0.0

# Run flask (windows)
flask run --host 0.0.0.0 --debug


# Run test
pytest -p no:warnings -vv



### 기타 (ubuntu 설정) ###
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
pip install -r requirements.txt
# or
pip install flask Flask-Cors PyJWT bcrypt mysql-connector-python

# 서버에서 flask 실행
nohup flask run --host 0.0.0.0 &

